入门阶段杂记，很乱，整理好的学习笔记在README里面


编译：
rm -rf build/ install/ log/
source /opt/ros/lyrical/setup.bash
colcon build





运行：
source install/setup.bash
ros2 launch ros2_homework_basic_package eight_figure.launch.py
ros2 launch topic_case_package topic_case.launch.py
ros2 launch param_case_package param_case.launch.py


rm -rf build/ install/ log/
source /opt/ros/lyrical/setup.bash
colcon build
source install/setup.bash
ros2 launch ros2_homework_basic_package eight_figure.launch.py





VSCodeUI：
包含路径：/opt/ros/*/include/**





CMakeLists：
编译错误警告：
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()
lint测试警告：
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()
ROS2固定结尾：
ament_package()
file(GLOB MSG_FILES RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}" "msg/*.msg")：把 msg 目录下所有 .msg 文件的列表（相对于当前源码目录的路径）存到变量 MSG_FILES 中。
visualization_msgs，有Marker、MarkerArray等





cpp：
explicit构造函数：
对于外部函数传入类的参数时，严格匹配类（初始化），如果只传入初始化会报错。

继承Node定义构造函数：
ParamCase(): 
Node("param_case"),...
{
//创建参数客户
param_client_=std::make_shared<rclcpp::SyncParametersClient>(this,turtlesim_node_name_）;
}

循环频率，用sleep补齐剩余时间：
rclcpp::Rate rate(loop_rate_hz_);
while (rclcpp::ok()) {...rate.sleep();}

lambda捕获[]：
函数定义当中的局部变量

main函数：
int main(int argc, char * argv[])
{
	// 2. 初始化 ROS2 客户端。
	rclcpp::init(argc, argv);

	// 4. 创建对象指针,并调用其函数。
	auto node = std::make_shared<ParamCase>();
	node->run();

	// 5. 释放资源。
	rclcpp::shutdown();
	return 0;
}

创建发布智能指针：
publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/circle_cmd", 10);
<消息类型>("/全局话题",队列长度缓存长度)

回调函数定时器：
timer_ = this->create_wall_timer(100ms,std::bind(&TopicPublisher::publish_circle_command, this));}
create_wall_timer每100ms触发一次publish_circle_command
bind将publish_circle_command与this绑定

节点对象持续运行并响应定时器：
rclcpp::spin(node);

创建订阅智能指针：
subscription_ = this->create_subscription<geometry_msgs::msg::Twist>(
      "/circle_cmd",
      10,
      std::bind(&TopicSubscriber::handle_circle_command, this, std::placeholders::_1));
(话题，缓存长度，bind(回调函数,this，将来收到的第一个参数）只要收到消息就触发回调函数。

订阅者将消息发布到官方定义的乌龟话题：
publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);


launch.py:
函数结构：
def generate_launch_description():return LaunchDescription([......])

拼接路径：PathJoinSubstitution([1,2,3,...])
查找路径：FindPackageShare('param_case_package')
读取配置文件，为本节点提供参数化的运行配置（这里是直接在launch文件里加载yaml文件了，如果不想的话可以用PPT上的命令在运行时加载）。
param_case_config = PathJoinSubstitution([FindPackageShare('param_case_package'), 'config', 'param_case.yaml'])
参数传入：parameters=[param_case_config]

查看消息类型：
ros2 interface show fsd_common_msgs/msg/Map
ros2 interface show fsd_common_msgs/msg/Cone

播放bag
source install/setup.bash
ros2 bag play src/map_to_visualize/map_to_visualize_0.db3 --loop

加载marker
source install/setup.bash
ros2 run map_to_visualize map_visualizer

加载.rviz预设：arguments=['-d', rviz_config],  # 加载预配置文件




xml:
编译时依赖<build_depend>rosidl_default_generators</build_depend>
运行时依赖<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>：声明本包属于“ROS 2 接口包”组

rm -rf build/ install/ log/
source /opt/ros/lyrical/setup.bash
colcon build
source install/setup.bash
ros2 launch map_to_visualize visualize_cones.launch.py

