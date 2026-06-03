"""
@file visualize_cones.launch.py
@brief ROS 2 Launch 文件：一键启动 bag 播放 + 可视化节点 + rviz2

使用方式：
    ros2 launch map_to_visualize visualize_cones.launch.py

此 launch 文件会同时启动以下三个组件：
    1. ros2 bag play（循环播放预录制的锥桶地图数据）
    2. map_visualizer 节点（订阅 /estimation/slam/map，发布 /cone_markers）
    3. rviz2（加载预配置的 cones.rviz，自动订阅 /cone_markers 并显示）
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    """
    生成 LaunchDescription 对象，Launch 系统根据此描述启动所有进程。

    get_package_share_directory() 的返回值：
        在 colcon build 之后，包的 share 目录位于 install/<pkg>/share/<pkg>/，
        其中包含 bag 数据文件（.db3 + metadata.yaml）、rviz 配置文件、launch 文件等。
        通过此函数可避免硬编码路径，使 launch 文件在任意环境下均可运行。
    """
    # 获取功能包的 share 目录路径
    pkg_dir = get_package_share_directory('map_to_visualize')

    # Bag 文件路径：CMakeLists.txt 将 .db3 和 metadata.yaml 安装到了 share 目录，
    # ros2 bag play 需要传入包含 metadata.yaml 的目录路径（.db3 文件名在 metadata 中指定）。
    bag_path = pkg_dir

    # RViz 配置文件路径：预配置了 Fixed Frame = "world"、订阅 /cone_markers 话题、
    # 以及四种颜色锥桶的命名空间筛选（cone_yellow/blue/red/unknown）。
    rviz_config = os.path.join(pkg_dir, 'rviz', 'cones.rviz')

    return LaunchDescription([
        # ----------------------------------------------------------------
        # 组件 1: 播放 ROS 2 bag 文件
        # ros2 bag play 从 .db3 文件中读取序列化消息，按原始时间戳重新发布到原话题。
        # --loop 参数使 bag 循环播放，方便在 rviz 中反复观察锥桶分布。
        # 发布的话题：/estimation/slam/map（类型 fsd_common_msgs/msg/Map）
        # ----------------------------------------------------------------
        ExecuteProcess(
            cmd=['ros2', 'bag', 'play', bag_path, '--loop'],
            output='screen',  # 将 bag play 的 stdout/stderr 输出到终端
        ),

        # ----------------------------------------------------------------
        # 组件 2: 运行锥桶可视化节点
        # 该节点订阅 /estimation/slam/map，将 Map 消息中的锥桶数据转换为
        # visualization_msgs/MarkerArray，发布到 /cone_markers 话题。
        # ----------------------------------------------------------------
        Node(
            package='map_to_visualize',   # 功能包名（与 package.xml 中的 <name> 一致）
            executable='map_visualizer',   # 可执行文件名（CMakeLists.txt 中 add_executable 的名称）
            name='map_visualizer',         # 运行时节点名称（可自定义，会覆盖代码中的节点名）
            output='screen',               # 将节点的日志输出到终端
        ),

        # ----------------------------------------------------------------
        # 组件 3: 启动 rviz2
        # -d 参数指定 rviz 配置文件，rviz 启动时会自动加载该配置。
        # cones.rviz 中已预设：
        #   - Fixed Frame = "world"（与 bag 数据的坐标系匹配）
        #   - 订阅 /cone_markers 话题的 MarkerArray 显示插件
        #   - 四种颜色命名空间均开启显示
        # ----------------------------------------------------------------
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],  # 加载预配置文件
            output='screen',
        ),
    ])
