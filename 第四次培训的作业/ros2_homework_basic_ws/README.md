# ROS2 基础作业 —— 控制海龟做8字形运动

---

## 一、代码启动命令流程

### 1.1 重置（亲测如果不重置就不成8字）：
rm -rf build/ install/ log/

### 1.2 编译代码：
source /opt/ros/lyrical/setup.bash
colcon build

### 1.3 运行代码：
source install/setup.bash
ros2 launch ros2_homework_basic_package eight_figure.launch.py

### 1.4 停止运行：
在启动终端按下 `Ctrl+C` 即可停止所有节点。

---

## 二、ROS学习笔记

### 2.1 核心概念回顾

#### 节点（Node）
- ROS2中的基本执行单元，一个节点负责一个相对独立的功能
- 本作业包含两个节点：`turtlesim_node`（仿真显示，ros2自带）和 `eight_figure_node`（运动控制，自定义，仅充当发布者），并没有自定义不必要的订阅者
- 节点通过话题（Topic）进行通信

#### 话题（Topic）与消息（Message）
- **话题**：节点之间发布/订阅数据的通道，采用发布-订阅模型
- **消息**：话题上传输的数据结构
- 本作业使用的关键话题：`/turtle1/cmd_vel`：`geometry_msgs/msg/Twist` 类型，控制海龟速度

#### Twist消息结构
```
geometry_msgs/msg/Twist {
  Vector3 linear {   // 线速度
    float64 x        // 前进/后退速度（本作业使用）
    float64 y        // 左右平移速度（2D运动中为0）
    float64 z        // 上下速度（2D运动中为0）
  }
  Vector3 angular {  // 角速度
    float64 x        // 横滚角速度（2D运动中为0）
    float64 y        // 俯仰角速度（2D运动中为0）
    float64 z        // 偏航角速度/转向速度（本作业使用）
  }
}
```

#### 参数（Parameter）
- ROS2中用于配置节点行为的键值对
- 本作业将线速度、角速度等配置为参数，便于调试和修改
- 参数可在launch文件中通过yaml文件传入

#### Launch文件
- 用于一次性启动多个节点和配置
- ROS2支持Python编写launch文件，比ROS1的XML格式更灵活
- 本作业使用launch文件同时启动turtlesim和控制节点

### 2.2 C++编程要点

#### 智能指针
- ROS2大量使用 `std::shared_ptr` 管理对象生命周期
- `create_publisher`、`create_timer` 等函数返回的都是智能指针
- 使用智能指针可以避免内存泄漏

#### Lambda表达式与std::bind
- `std::bind(&EightFigureNode::timerCallback, this)` 将成员函数绑定到当前对象
- 也可以使用lambda表达式：`[this]() { timerCallback(); }`（捕获外部this指针）
- 这两种方式都能创建可被定时器调用的回调函数对象

#### 时间管理
- `rclcpp::Time`：ROS时间类型，支持时间运算
- `rclcpp::Duration`：时间间隔类型，表示两个Time的差值
- `std::chrono`：C++标准库时间库，用于设置定时器周期

---

## 三、作业完成思路

### 3.1 设计过程

**步骤1：确定运动算法**
- 分析8字形 = 两个相切圆
- 确定通过切换角速度方向实现8字形
- 保证线速度始终为正，确保两圆相切

**步骤2：确定文件结构**
```
ros2_homework_basic_package/
├── config/trajectory_params.yaml   # 参数配置
├── launch/eight_figure.launch.py   # 启动文件
├── src/eight_figure_node.cpp       # 控制节点源码
├── CMakeLists.txt                  # 编译配置
└── package.xml                     # 包配置
```

**步骤3：编码实现**
- 编写节点类，继承 `rclcpp::Node`
- 实现参数声明和读取
- 实现定时器回调，周期性地发布速度指令
- 根据时间判断当前处于哪个半周期，切换角速度方向

**步骤4：配置和测试**
- 编写launch文件，同时启动turtlesim和控制节点
- 编写yaml参数文件
- 编译并运行测试

### 3.3 代码架构

```
eight_figure_node.cpp
├── EightFigureNode 类
│   ├── 构造函数
│   │   ├── 声明参数 (declare_parameter)（默认值 or 被yaml文件读取覆盖）
│   │   ├── 获取参数 (get_parameter)
│   │   ├── 创建发布者 (create_publisher)
│   │   ├── 创建定时器 (create_wall_timer)
│   │   └── 初始化状态变量
│   └── timerCallback 回调函数
│       ├── 计算经过时间
│       ├── 判断当前阶段（第一个圆 / 第二个圆）
│       ├── 构造 Twist 消息
│       └── 发布速度指令
└── main 函数
    ├── rclcpp::init()
    ├── 创建节点
    ├── rclcpp::spin()
    └── rclcpp::shutdown()
```

---

## 四、完成作业遇到的困难以及解决办法

### 困难1：如何确保两个圆相切？

**问题描述**：一开始考虑在每个圆结束时停止海龟，然后调整方向再启动。但这样会导致两个圆不相切，中间有停顿。

**解决办法**：
- 研究后发现，**只要线速度方向不变，角速度方向反转，两个圆就在切换点自然相切**
- 原因：角速度的突变只改变曲率方向，不改变运动方向（切线方向）
- 最终方案：线速度始终为正，角速度周期性地在 `+ω` 和 `-ω` 之间切换

### 困难2：参数文件路径问题

**问题描述**：一开始在launch文件中使用相对路径 `config/trajectory_params.yaml`，导致找不到文件。

**解决办法**：
- 学习 `ament_index_python` 包中的 `get_package_share_directory()` 函数
- 使用该函数获取包的绝对路径，再拼接配置文件路径
- 这样无论从哪里启动launch文件，都能找到正确的配置文件

### 困难3：重置问题
**问题描述**：第一次运行符合预期，第二次以后就不成8字。

**解决办法**：
rm -rf build / install / log 重置项目环境，让每一次运行都是第一次运行。


---

## 五、AI使用情况

本作业在以下环节使用了AI辅助：

1. **代码框架生成**：使用AI生成ROS2节点的基本框架（类结构、main函数等）
2. **问题排查**：遇到编译错误时，使用AI帮助分析错误信息
3. **文档排版**：使用AI生成README模板让我填写

---

## 六、项目文件结构

```
ros2_homework_basic_ws/
├── build/                              # 编译中间文件（自动生成）
├── install/                            # 编译输出文件（自动生成）
├── log/                                # 编译日志（自动生成）
├── src/
│   └── ros2_homework_basic_package/    # 功能包
│       ├── config/
│       │   └── trajectory_params.yaml  # 运动参数配置文件
│       ├── launch/
│       │   └── eight_figure.launch.py  # launch启动文件
│       ├── src/
│       │   └── eight_figure_node.cpp   # 控制节点C++源码
│       ├── result/                     # 可视化结果（截图、视频等）
│       ├── CMakeLists.txt              # CMake编译配置
│       └── package.xml                 # ROS2包配置
└── README.md                           # 本文件
```
