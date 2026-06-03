"""
本launch文件完成以下任务：
1. 启动 turtlesim_node 节点（提供可视化海龟仿真环境）
2. 加载参数配置文件（trajectory_params.yaml）
3. 启动 eight_figure_node 节点（控制海龟做8字形运动）

Launch文件原理：
- Launch文件使用Python编写，通过LaunchDescription描述要启动的节点和配置
- 节点之间的启动顺序由ROS2的launch系统自动管理
- 参数通过Node对象的parameters参数传入

使用方法：
  ros2 launch ros2_homework_basic_package eight_figure.launch.py
"""

# 导入必要的库

# os.path 模块：提供路径操作函数（如join、abspath等）
# 用于构建配置文件的绝对路径，确保无论在哪个目录运行launch文件都能找到配置文件
import os

# ament_index_python.packages 模块：提供ROS2包索引查询功能
# get_package_share_directory() 可以获取指定ROS2包的共享目录路径
from ament_index_python.packages import get_package_share_directory

# launch 模块：ROS2 launch系统的核心模块
# LaunchDescription：launch文件的顶层描述对象，包含所有要启动的内容
# launch_actions：包含各种启动动作（如启动节点、执行命令等）
from launch import LaunchDescription
from launch_ros.actions import Node  # Node：用于启动ROS2节点的动作


def generate_launch_description():
    """
    这是launch文件的入口函数，ROS2 launch系统会调用此函数获取启动配置。
    函数名必须是 generate_launch_description，这是launch系统的约定。
    """

    # 获取包目录路径
    # get_package_share_directory() 返回包的share目录路径
    # 这是ROS2安装结构中的标准目录，包含launch、config等子目录
    # 在开发工作空间中，通常是：<ws>/install/<package>/share/<package>
    pkg_share = get_package_share_directory('ros2_homework_basic_package')

    # 构建参数文件路径
    # os.path.join() 智能地拼接路径，自动处理不同操作系统的路径分隔符
    # ('/' for Linux/macOS, '\\' for Windows)
    # 配置文件位于包的config目录下
    params_file = os.path.join(pkg_share, 'config', 'trajectory_params.yaml')

    # 打印参数文件路径，便于调试
    print(f"[Launch] 参数文件路径: {params_file}")

    # 创建LaunchDescription对象
    # LaunchDescription是launch文件的核心对象
    # 它接收一个列表，列表中的每个元素都是一个"动作"（Action）
    # 动作包括：启动节点、执行命令、设置参数等
    return LaunchDescription([
        # 启动 turtlesim_node 节点
        # turtlesim_node 是ROS2官方提供的海龟仿真器节点
        # 它提供了一个可视化窗口，显示海龟的运动轨迹
        # 节点会自动创建话题 /turtle1/cmd_vel 和 /turtle1/pose
        Node(
            package='turtlesim',          # 包名：turtlesim是ROS2官方仿真包
            executable='turtlesim_node',  # 可执行文件名：turtlesim的主节点
            name='turtlesim',             # 节点名称：在ROS2网络中的标识
            output='screen',              # 输出方式：'screen'表示输出到终端
            # parameters=[]  # turtlesim_node不需要额外参数
        ),

        # 启动 eight_figure_node 节点
        # eight_figure_node 是我们自己编写的控制节点
        # 它会读取参数文件中的配置，并控制海龟做8字形运动
        Node(
            package='ros2_homework_basic_package',  # 包名：我们自己的功能包
            executable='eight_figure_node',          # 可执行文件名：编译后生成的可执行文件
            name='eight_figure_node',                # 节点名称
            output='screen',                         # 输出方式：输出到终端
            # parameters：传入参数文件路径
            # ROS2会自动解析yaml文件，并将参数值传入节点的参数服务器，覆盖默认值
            # 节点内部通过 this->get_parameter() 即可读取这些参数
            parameters=[params_file],
        ),
    ])
