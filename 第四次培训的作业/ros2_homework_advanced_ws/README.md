# ROS 2 进阶作业：锥桶地图可视化（Cone Map Visualizer）

## 一、项目概述

目标：将已录制的 bag 文件中的锥桶地图数据，通过自定义节点转换为 `visualization_msgs/MarkerArray`，并在 **rviz2** 中实时可视化显示。

**可视化内容**：
- 黄色锥桶（yellow）—— 用黄色球体表示
- 蓝色锥桶（blue）—— 用蓝色球体表示
- 红色锥桶（red）—— 用红色球体表示
- 未知颜色锥桶（unknown）—— 用灰色球体表示

**核心文件**：

| 文件 | 作用 |
|------|------|
| `src/map_visualizer.cpp` | 可视化节点源码（订阅 Map 然后 发布 MarkerArray） |
| `launch/visualize_cones.launch.py` | Launch 文件，一键启动全部组件 |
| `rviz/cones.rviz` | rviz2 预配置文件（坐标系、话题订阅已配好） |
| `CMakeLists.txt` / `package.xml` | 功能包编译配置 |
| `map_to_visualize_0.db3` / `metadata.yaml` | 提供的 bag 数据文件 |

---

## 二、环境依赖

| 依赖项 | 说明 |
|--------|------|
| ROS 2 Lyrical | 系统级 ROS 2 发行版 |
| `rclcpp` | ROS 2 C++ 客户端库 |
| `visualization_msgs` | rviz2 可视化消息定义（含 Marker、MarkerArray） |
| `fsd_common_msgs` | 自定义消息包（含 Map.msg、Cone.msg 等） |
| `ros-lyrical-can-msgs` | fsd_common_msgs 的间接依赖 |

---

## 三、编译步骤

```bash
source /opt/ros/lyrical/setup.bash
colcon build
source install/setup.bash
```

---

## 四、启动命令流程

提供两种启动方式：**Launch 一键启动（推荐）**和**分步手动启动（调试用）**。

### 4.1 方式一：Launch 一键启动（推荐）

一条命令同时启动 bag 播放、可视化节点和 rviz2：

```bash
source /opt/ros/lyrical/setup.bash
source install/setup.bash
ros2 launch map_to_visualize visualize_cones.launch.py
```

launch 文件会自动完成以下三件事：
1. `ros2 bag play <bag_path> --loop` —— 循环播放预录制数据
2. 启动 `map_visualizer` 节点 —— 转换 Map 到 MarkerArray
3. 启动 `rviz2 -d cones.rviz` —— 加载预配置的可视化界面

rviz2 窗口打开后，即可在主视图中看到各色锥桶球体。由于 rviz 配置文件已预设 `Fixed Frame = "world"`，无需手动修改坐标系。

### 4.2 方式二：分步手动启动（调试用）

当你需要逐步排查问题、观察每个环节的输出时，可以在三个终端中分别启动：

**终端 1 —— 播放 bag 文件**：
```bash
source /opt/ros/lyrical/setup.bash
source install/setup.bash
ros2 bag play src/map_to_visualize/map_to_visualize_0.db3 --loop
```
- `--loop` 表示循环播放，方便反复观察。
- bag 中只包含一个话题 `/estimation/slam/map`，消息类型为 `fsd_common_msgs/msg/Map`，共 292 条消息。

**终端 2 —— 启动可视化节点**：
```bash
source /opt/ros/lyrical/setup.bash
source install/setup.bash
ros2 run map_to_visualize map_visualizer
```

**终端 3 —— 启动 rviz2 并手动配置**：
```bash
source /opt/ros/lyrical/setup.bash
rviz2
```

rviz2 手动配置步骤：
1. Fixed Frame 设置为 `world`。

2. 添加 MarkerArray 显示插件

---

## 五、ROS 2 学习笔记

### 5.1 ROS 2 核心概念

#### 5.1.1 工作空间（Workspace）

ROS 2 工作空间是一个包含源码（`src/`）、编译产物（`build/`）和安装产物（`install/`）的目录结构：

```
ros2_homework_advanced_ws/
├── src/        # 源码目录，每个子目录是一个功能包
├── build/      # colcon build 的中间产物（CMake 缓存、目标文件等）
├── install/    # colcon build 的安装产物（可执行文件、库、share 数据等）
└── log/        # 编译日志
```

##### 编译规则
`colcon build` 遍历 `src/` 下所有功能包，编译后将产物放入 `install/`。运行节点前必须 `source install/setup.bash`，它会将 `install/` 下的路径加入 `PATH`、`LD_LIBRARY_PATH` 等环境变量。

#### 5.1.2 功能包（Package）

ROS 2 功能包是代码的组织单元，由 `package.xml`（元信息）和 `CMakeLists.txt`（编译规则，C++ 包）或 `setup.py`/`setup.cfg`（Python 包）定义。

本项目有两个功能包：
- **`fsd_common_msgs`**：纯消息定义包。`package.xml` 声明了 `<member_of_group>rosidl_interface_packages</member_of_group>`，CMakeLists.txt 使用 `rosidl_generate_interfaces()` 生成消息的 C++/Python 代码。
- **`map_to_visualize`**：可执行节点包。依赖 `fsd_common_msgs` 的消息定义，编译出 `map_visualizer` 可执行文件。

#### 5.1.3 消息（Message）

ROS 2 中，节点间通过**话题（Topic）**传递**消息（Message）**。消息由 `.msg` 文件定义，编译后生成对应的 C++/Python 结构体。

本项目涉及的消息类型：

| 消息类型 | 定义所在 | 字段说明 |
|----------|----------|----------|
| `fsd_common_msgs/msg/Map` | `fsd_common_msgs/msg/Map.msg` | `std_msgs/Header header` + 四个 Cone 数组（cone_yellow/blue/red/unknown） |
| `fsd_common_msgs/msg/Cone` | `fsd_common_msgs/msg/Cone.msg` | `geometry_msgs/Point position`、`string color`、`float64 pose_confidence`、`float64 color_confidence` |
| `visualization_msgs/msg/MarkerArray` | ROS 2 标准消息 | `Marker[] markers`，rviz2 原生的可视化消息格式 |
| `visualization_msgs/msg/Marker` | ROS 2 标准消息 | 单个可视化对象，包含 header、ns、id、type、pose、scale、color、lifetime 等字段 |

消息编译后生成的 C++ 头文件位于 `install/fsd_common_msgs/include/`，可直接 `#include "fsd_common_msgs/msg/map.hpp"` 使用。

#### 5.1.4 话题（Topic）

话题是节点间**异步通信**的通道，采用**发布-订阅（Pub-Sub）**模型：
- 发布者（Publisher）将消息发送到某个话题名；
- 订阅者（Subscriber）注册对该话题的兴趣，当有新消息到达时触发回调函数。
- 发布者和订阅者彼此**解耦**：它们不需要知道对方的存在，只通过话题名匹配。

**常用调试命令**：
```bash
# 列出当前所有活跃话题
ros2 topic list

# 查看某话题的详细信息（类型、发布者数量、订阅者数量）
ros2 topic info /estimation/slam/map

# 查看话题的发布频率
ros2 topic hz /estimation/slam/map

# 打印话题的消息内容（用于调试）
ros2 topic echo /estimation/slam/map

# 查看消息类型定义
ros2 interface show fsd_common_msgs/msg/Map
ros2 interface show fsd_common_msgs/msg/Cone
```

### 5.2 rviz2 与 Marker

rviz2 是 ROS 2 自带的 3D 可视化工具，可显示点云、机器人模型、Marker、图像、TF 坐标变换等。

#### 5.2.1 Marker 的关键字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `header.frame_id` | string | Marker 所在的**坐标系名称**，必须与 rviz 的 Fixed Frame 匹配才能显示 |
| `header.stamp` | builtin_interfaces/Time | 时间戳，lifetime 从此时间开始计算 |
| `ns` (namespace) | string | 命名空间，用于分类管理 Marker；rviz 可按 ns 单独显隐 |
| `id` | int32 | 命名空间内的唯一标识；同一 `ns:id` 的后续消息会覆盖之前的 Marker |
| `type` | int32 | 几何形状：`SPHERE`(球体)、`CUBE`(立方体)、`CYLINDER`(圆柱体)、`ARROW`(箭头)、`TEXT_VIEW_FACING`(文字) 等 |
| `action` | int32 | 操作类型：`ADD`(添加/更新)、`DELETE`(删除指定 id)、`DELETEALL`(删除该 ns 下全部) |
| `pose` | geometry_msgs/Pose | 位置（position）和姿态（orientation 四元数） |
| `scale` | geometry_msgs/Vector3 | 尺寸缩放（x/y/z），对 SPHERE 表示三个方向的直径 |
| `color` | std_msgs/ColorRGBA | RGBA 颜色，每个分量范围 [0.0, 1.0] |
| `lifetime` | builtin_interfaces/Duration | 显示持续时间；0 表示永久显示；正值表示到期后自动删除 |

#### 5.2.2 旧 Marker 清理策略

锥桶地图是**动态变化**的（不同帧的锥桶数量可能不同），因此需要清理上一帧的旧 Marker，避免"重影"或"残留"。ROS 2 提供了两种策略：

**策略 A：DELETEALL 显式清理**
- 在每帧开始时，对每个命名空间发送 `action=DELETEALL` 的 Marker；
- rviz 收到后删除该 ns 下的所有 Marker，然后发送新 Marker（`action=ADD`）覆盖；
- 优点：逻辑清晰，显式控制；需配合 `lifetime=0`（永久显示）。
- 缺点：代码量稍大；若 DELETEALL 因网络乱序晚于 ADD 到达，会误删新 Marker。

**策略 B：lifetime 自动过期**（本代码采用）
- 将每个 Marker 的 `lifetime` 设为较短值（0.15 秒）；
- rviz 内部计时器到期后自动删除该 Marker，新帧到达时重新创建，天然处理动态增减；
- 优点：代码简洁，无乱序风险；
- 缺点：若消息发布频率低于 `1/lifetime`，Marker 会先消失再出现（闪烁）。本 bag 约 10Hz 发布，帧间隔约 0.1s，lifetime=0.15s > 0.1s，恰好覆盖两帧间隔，不会闪烁。

### 5.3 坐标系（Frame）

#### 5.3.1 核心概念

坐标系（Frame）是 ROS 中定位物体的基准。每个几何数据（点、位姿、Marker）都关联一个 `frame_id`，表示该数据在**哪个坐标系**下定义。

rviz 显示 Marker 的条件：rviz 的 Fixed Frame 与 Marker 的 `header.frame_id` 之间选一个：
1.必须存在坐标变换（TF）2.两者名称完全一致（表示同一坐标系）。

#### 5.3.2 本项目的坐标系问题

| 组件 | 使用的坐标系 | 来源 |
|------|-------------|------|
| bag 中的 Map 消息 | `world` | `msg->header.frame_id` |
| map_visualizer 发布的 Marker | `world`（原样传递） | 从 Map.header 读取 |
| rviz2 默认 Fixed Frame | `map` | rviz2 出厂默认值 |

**问题**：bag 数据用 `world` 坐标系，但 rviz2 默认用 `map` 坐标系。由于系统中没有 TF 变换发布者，rviz 无法渲染 Marker。

**解决方法**：
修改 rviz Fixed Frame：在 rviz 中将 Fixed Frame 手动改为 `"world"`。本项目提供的 `rviz/cones.rviz` 已预设此项。


---

## 六、作业完成思路

### 6.1 大概过程

1. **分析 bag 数据**：用 `ros2 bag info` 查看话题和消息类型，确认输入为 `/estimation/slam/map`（`fsd_common_msgs/msg/Map`）。
2. **阅读消息定义**：用 `ros2 interface show` 查看 `Map.msg` 和 `Cone.msg`，理解消息结构（header + 四个 Cone 数组）。
3. **设计可视化方案**：选用 `visualization_msgs/MarkerArray`，每种颜色锥桶对应一个命名空间，用 SPHERE 表示锥桶位置。
4. **编写订阅节点**：创建 `MapVisualizer` 类，订阅 `/estimation/slam/map`，实现回调函数 `map_callback`。
5. **编写 Marker 生成逻辑**：遍历四种颜色数组，调用 `make_cone_marker` 工厂函数生成 Marker。
6. **处理坐标系**：从消息 header 中读取 `frame_id`（值为 `world`），原样赋给 Marker，由用户在 rviz 中同步设置 Fixed Frame。
7. **编译测试**：编译功能包，运行 bag + 节点 + rviz2，验证可视化效果。

### 6.2 关键设计决策

| 决策点 | 选择 | 理由 |
|--------|------|------|
| Marker 类型 | SPHERE（球体） | 简单直观，无需考虑朝向；CYLINDER 可更逼真但需调姿态 |
| 球体直径 | 0.3 m | 接近真实锥桶底面直径，rviz 中观感适中 |
| 清理策略 | lifetime=0.15s 自动过期 | 代码更简洁，无乱序风险（详见 5.2.2 节策略对比） |
| 坐标系处理 | 原样传递 frame_id，手动改 rviz | 保持数据原始语义，不硬编码 |
| 颜色映射 | 黄→(1,1,0)、蓝→(0,0,1)、红→(1,0,0)、未知→灰(0.5,0.5,0.5) | 与真实锥桶颜色对应，未知色用灰色区分 |
| 命名空间 | `cone_yellow`、`cone_blue`、`cone_red`、`cone_unknown` | 支持 rviz 中按颜色单独显隐，方便调试 |

---

## 七、遇到的困难及解决办法

### 困难 1：`can_msgs` 包找不到，编译失败

**现象**：编译 `fsd_common_msgs` 时 CMake 报错 。

**原因**：`fsd_common_msgs` 的 `package.xml` 和 `CMakeLists.txt` 中声明了对 `can_msgs` 的依赖，但系统中未安装该包。`can_msgs` 是 ROS 2 的 CAN 总线标准消息包。

**解决**：
```bash
sudo apt install ros-lyrical-can-msgs
```

### 困难 2：中文路径导致 rosidl_adapter 解析错误

**原因**：工作空间位于 `~/桌面/`（路径含 UTF-8 中文字符）。
**解决**：显式指定 UTF-8 编码：
```cmake
file(STRINGS "${idl_output}" idl_tuples ENCODING UTF-8)
```

**知识点**：CMake 的 `file(STRINGS)` 默认按当前系统 locale 解析行终止符。中文 UTF-8 编码中，某些字节（如 0xE6 等）在非 UTF-8 的 locale 下可能被误判为 `\n` 或 `\r`。

### 困难 3：`geometry_msgs/Pose2D` 在 ROS 2 Lyrical 中已被移除（我安装的Ubuntu26.04，适配ROS2 Lyrical，版本不合造成困难）

**现象**：编译 `fsd_common_msgs` 时找不到 `Pose2D.json`。

**原因**：`CarState.msg` 和 `CarStateDt.msg` 中引用了 `geometry_msgs/Pose2D`，该消息类型在 ROS 2 较新版本（Lyrical）中已从 `geometry_msgs` 包中删除。

**解决**：在 `fsd_common_msgs` 包内自定义 `Pose2D.msg`：
```
float64 x
float64 y
float64 theta
```
并将 `CarState.msg` 和 `CarStateDt.msg` 中对 `geometry_msgs/Pose2D` 的引用改为 `fsd_common_msgs/Pose2D`。

### 困难 4：`map_to_visualize` 缺少包配置文件

**现象**：`colcon build` 编译报错。

**原因**：`map_to_visualize` 目录下只有一个 `src/map_visualizer.cpp`，缺少 ROS 2 功能包必需的 `CMakeLists.txt` 和 `package.xml`。colcon 只识别包含 `package.xml` 的目录为功能包。

**解决**：创建 `CMakeLists.txt` 和 `package.xml`。其中 `CMakeLists.txt` 注意 ROS 2 Lyrical 已移除 `ament_target_dependencies`，改用 `target_link_libraries` 直接链接 imported targets

**知识点**：ROS 2 中消息类型需要在 CMakeLists.txt 中显式链接。

### 困难 5：rviz2 中看不到 Marker

**现象**：节点和 bag 都正常运行，终端日志正常输出锥桶数量，但 rviz2 中没有任何锥桶显示。

**根本原因**：rviz2 的 `Fixed Frame` 默认是 `"map"`，bag 数据的坐标系是 `"world"`，两者不一致导致坐标变换失败。

**解决**：在 rviz2 左侧 `Global Options` → `Fixed Frame` 中手动改为 `"world"`。本项目的 `rviz/cones.rviz` 已预设此项，使用 launch 文件启动可避免此问题。

### 困难 6：launch 文件找不到 bag 或 rviz 配置文件

**现象**：`ros2 launch` 报错找不到 `.db3` 或 `.rviz` 文件。

**原因**：launch 文件中使用 `get_package_share_directory()` 获取路径，该函数返回的是 `install/<pkg>/share/<pkg>/` 目录。如果 `CMakeLists.txt` 中没有 `install()` 命令将文件安装到 share 目录，launch 就找不到它们。

**解决**：在 `CMakeLists.txt` 中添加：
```cmake
install(DIRECTORY launch rviz
  DESTINATION share/${PROJECT_NAME})
install(FILES map_to_visualize_0.db3 metadata.yaml
  DESTINATION share/${PROJECT_NAME})
```
每次修改 launch/rviz 文件或 bag 数据后，需要重新 `colcon build`。

---

## 八、快速参考命令

```bash
# ========== 编译 ==========
source /opt/ros/lyrical/setup.bash
colcon build 
source install/setup.bash

# ========== 一键启动 ==========
ros2 launch map_to_visualize visualize_cones.launch.py

# ========== 分步启动（调试用） ==========
# 终端 1
ros2 bag play src/map_to_visualize/map_to_visualize_0.db3 --loop
# 终端 2
ros2 run map_to_visualize map_visualizer
# 终端 3
rviz2 -d src/map_to_visualize/rviz/cones.rviz

# ========== 查看消息定义 ==========
ros2 interface show fsd_common_msgs/msg/Map
ros2 interface show fsd_common_msgs/msg/Cone
ros2 interface show visualization_msgs/msg/Marker

# ========== 查看话题 ==========
ros2 topic list                          # 列出所有话题
ros2 topic info /estimation/slam/map     # 查看话题详情
ros2 topic echo /cone_markers            # 打印 MarkerArray 内容
ros2 topic hz /estimation/slam/map       # 查看发布频率

# ========== 查看 bag 信息 ==========
ros2 bag info src/map_to_visualize/map_to_visualize_0.db3

# ========== 查看节点图 ==========
rqt_graph                                 # 图形化显示节点和话题关系
```

---

## 九、文件结构

```
map_to_visualize/
├── CMakeLists.txt                 # 编译配置（目标、依赖、安装规则）
├── package.xml                    # 功能包元信息（名称、版本、依赖声明）
├── README.md                      # 本说明文档
├── map_to_visualize_0.db3         # bag 数据（SQLite3 格式，存放序列化消息）
├── metadata.yaml                  # bag 元数据（话题列表、消息数量、时长、QoS）
├── launch/
│   └── visualize_cones.launch.py  # Launch 文件（一键启动 bag + 节点 + rviz2）
├── rviz/
│   └── cones.rviz                 # rviz2 预配置文件（Fixed Frame: world，订阅 /cone_markers）
└── src/
    └── map_visualizer.cpp         # 可视化节点源码（Map → MarkerArray 转换）
```

---

## 十、补充说明

### 10.1 关于 fsd_common_msgs 功能包

`fsd_common_msgs` 是使用的自定义消息包，它不包含源文件（.cpp/.py），仅定义 `.msg` 消息格式。这是 ROS 2 中"接口包（Interface Package）"的标准模式——只定义消息/服务/动作，不包含可执行代码。

**接口包的工作方式**：
- `CMakeLists.txt` 使用 `rosidl_generate_interfaces()` 从 `.msg` 文件生成 C++ 和 Python 绑定；
- 编译后，其他功能包可通过 `find_package(fsd_common_msgs)` 找到并链接；

### 10.2 关于 Lifetime 与发布频率的关系

`lifetime` 参数的单位是秒，从 `header.stamp` 开始计时（不是从收到消息的时间开始）。本代码中 `header.stamp = this->now()`，即 Marker 创建时刻。

**设计原则**：`lifetime > 1 / 发布频率`，确保相邻两帧之间有重叠，不会闪烁。
- 本 bag 约 10Hz 发布（292 条 / 29 秒 ≈ 10 Hz），帧间隔 ≈ 0.1s；
- `lifetime = 0.15s > 0.1s`，满足条件。

若发布频率不稳定（如网络延迟导致间隔变大），增大 `lifetime` 值可增加容错空间，但会使已消失的锥桶残留更久。
