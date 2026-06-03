/**
 * 8字形轨迹由两个相切的圆组成：
 * 1. 第一个圆：海龟以恒定角速度逆时针（或顺时针）画一个圆
 * 2. 第二个圆：海龟切换到相反的旋转方向，画另一个圆
 * 3. 两个圆在切点处相切，形成连续的8字形轨迹
 *
 * 运动原理：
 * - 当线速度和角速度均为常数时，海龟的轨迹是一个圆
 * - 圆的半径 r = v / ω （线速度除以角速度）
 * - 画一个完整圆所需时间 T = 2π / |ω|
 * - 通过定时切换角速度的正负号，实现8字形轨迹
 *
 * 相切保证：
 * - 两个圆在第一个圆的终点（第二个圆的起点）处相切
 * - 切换方向时，线速度方向保持不变（始终向前）
 * - 角速度方向反转，使得第二个圆的弯曲方向相反
 * - 这样两个圆就在切换点处自然相切
 */

#include <chrono>           // C++标准库：提供时间相关功能（如秒、毫秒等）
#include <cmath>            // C++标准库：提供数学函数（如M_PI、sin、cos等）
#include <string>           // C++标准库：字符串类

#include "rclcpp/rclcpp.hpp"                    // ROS2 C++客户端库核心头文件
#include "geometry_msgs/msg/twist.hpp"          // ROS2 Twist消息类型，用于发布速度指令

/**
 * 该类实现了以下功能：
 * 1. 从参数服务器读取运动参数（线速度、角速度、周期、控制频率）
 * 2. 创建定时器，以固定频率发布速度指令
 * 3. 根据时间切换角速度方向，实现8字形轨迹
 * 4. 输出调试信息，便于观察运行状态
 */
class EightFigureNode : public rclcpp::Node {
 public:
  /**
   * 构造函数中完成以下初始化工作：
   * 1. 调用父类Node的构造函数
   * 2. 声明并获取参数
   * 3. 创建发布者（Publisher）
   * 4. 创建定时器（Timer）
   * 5. 初始化状态变量
   */
  explicit EightFigureNode(const std::string &node_name) : Node(node_name) {
    // 声明参数
    // ROS2中参数必须先声明（declare_parameter）才能使用
    // 这样可以让参数系统知道这些参数的存在，并支持从launch文件或命令行传入
    // declare_parameter<类型>("参数名", 默认值) -- 默认值在参数未提供时使用
    this->declare_parameter<double>("linear_velocity", 1.0);   // 线速度默认值 1.0 m/s
    this->declare_parameter<double>("angular_velocity", 1.0);  // 角速度默认值 1.0 rad/s
    this->declare_parameter<double>("period", 6.283185307);     // 单个圆周期默认值 2π 秒
    this->declare_parameter<int>("loop_rate", 100);            // 控制频率默认值 100 Hz

    // 获取参数值
    // get_parameter() 从参数服务器读取参数的实际值
    // 这些值可以在launch文件中通过params_file指定，也可以通过命令行传入
    linear_velocity_ = this->get_parameter("linear_velocity").as_double();
    angular_velocity_ = this->get_parameter("angular_velocity").as_double();
    period_ = this->get_parameter("period").as_double();
    loop_rate_ = this->get_parameter("loop_rate").as_int();

    // 打印参数信息
    // RCLCPP_INFO 是ROS2的日志宏，用于输出信息级别（INFO）的日志
    // 类似于C语言中的printf，但会添加时间戳和节点名称等元信息
    RCLCPP_INFO(this->get_logger(),
                "============================================");
    RCLCPP_INFO(this->get_logger(), "8字形运动参数配置：");
    RCLCPP_INFO(this->get_logger(), "  线速度 (linear_velocity): %.3f m/s", linear_velocity_);
    RCLCPP_INFO(this->get_logger(), "  角速度 (angular_velocity): %.3f rad/s", angular_velocity_);
    RCLCPP_INFO(this->get_logger(), "  单个圆周期 (period): %.3f s", period_);
    RCLCPP_INFO(this->get_logger(), "  控制频率 (loop_rate): %d Hz", loop_rate_);
    RCLCPP_INFO(this->get_logger(), "  轨迹半径 (radius): %.3f m", linear_velocity_ / angular_velocity_);
    RCLCPP_INFO(this->get_logger(),
                "============================================");

    // 创建发布者（Publisher）
    // create_publisher<消息类型>("话题名", QoS队列深度)
    // - 消息类型：geometry_msgs::msg::Twist，这是ROS2中标准的速度指令消息
    // - 话题名："/turtle1/cmd_vel"，这是turtlesim节点接收速度指令的标准话题
    // - QoS队列深度：10，表示如果消息处理不过来，最多缓存10条消息
    //
    // Twist消息结构说明：
    // Twist {
    //   Vector3 linear   -- 线速度向量（x: 前进/后退, y: 左右平移, z: 上下）
    //   Vector3 angular  -- 角速度向量（x: 横滚, y: 俯仰, z: 偏航/转向）
    // }
    // 对于2D平面运动的 turtlesim：
    // - linear.x 控制前进后退速度
    // - angular.z 控制转向速度（绕Z轴旋转）
    cmd_vel_pub_ = this->create_publisher<geometry_msgs::msg::Twist>(
        "/turtle1/cmd_vel", 10);

    // 创建定时器（Timer）
    // create_wall_timer(周期, 回调函数)
    // 周期：定时器触发的时间间隔，这里使用控制频率计算
    //   std::chrono::milliseconds(1000 / loop_rate_) 表示每多少毫秒触发一次
    // 回调函数：每次定时器触发时执行的函数，这里使用lambda表达式
    //   std::bind(&EightFigureNode::timerCallback, this) 将成员函数绑定到当前对象
    timer_ = this->create_wall_timer(
        std::chrono::milliseconds(1000 / loop_rate_),
        std::bind(&EightFigureNode::timerCallback, this));

    // 初始化状态变量
    // start_time_ 记录节点启动时间，用于计算经过的时间
    // rclcpp::Node::now() 返回当前ROS时间（rclcpp::Time类型）
    start_time_ = this->now();

    RCLCPP_INFO(this->get_logger(), "节点初始化完成，开始8字形运动...");
  }

 private:
  /**
   * 这是本节点的核心逻辑，完成以下任务：
   * 1. 计算从启动到现在经过的时间（elapsed_time）
   * 2. 根据当前处于哪个半周期，决定角速度的方向
   * 3. 构造并发布Twist速度指令消息
   * 4. 输出调试信息
   */
  void timerCallback() {
    // 计算从启动到现在经过的时间（elapsed_time）
    // this->now() 获取当前ROS时间
    // start_time_ 是节点启动时记录的时间
    // 两者相减得到经过的时间（rclcpp::Duration类型）
    // .seconds() 将Duration转换为秒（double类型）
    auto elapsed_time = (this->now() - start_time_).seconds();

    // 计算当前处于哪个半周期（phase）
    // fmod(elapsed_time, 2 * period_) 计算当前时间在完整8字周期中的位置
    // 一个完整的8字 = 两个圆，每个圆的周期为 period_
    // 因此完整的8字周期为 2 * period_
    // fmod是取余函数
    // 如果 phase < period_：处于第一个圆（例如逆时针）
    // 如果 phase >= period_：处于第二个圆（顺时针，角速度反向）
    double phase = fmod(elapsed_time, 2.0 * period_);

    // 确定当前角速度的方向
    // 角速度方向决定海龟转弯的方向：
    // 正值：逆时针旋转（数学上的正方向）
    // 负值：顺时针旋转
    //
    // 8字形的实现原理：
    // 在第一个半周期（phase < period_），使用正向角速度画第一个圆
    // 在第二个半周期（phase >= period_），使用负向角速度画第二个圆
    // 两个圆在切换点处相切，因为线速度方向始终向前
    double current_angular_velocity = angular_velocity_;
    if (phase >= period_) {
      current_angular_velocity = -angular_velocity_;  // 第二个圆，反向旋转
    }

    // 构造Twist消息
    // 创建Twist消息对象，默认所有字段为0
    // geometry_msgs::msg::Twist 包含两个Vector3：linear和angular
    auto twist_msg = geometry_msgs::msg::Twist();

    // 设置线速度（沿X轴前进）
    // linear.x > 0：向前运动
    // linear.x < 0：向后运动
    // linear.y 和 linear.z 在2D平面运动中通常为0
    twist_msg.linear.x = linear_velocity_;
    twist_msg.linear.y = 0.0;
    twist_msg.linear.z = 0.0;

    // 设置角速度（绕Z轴旋转）
    // angular.z > 0：逆时针旋转（CCW，Counter-Clockwise）
    // angular.z < 0：顺时针旋转（CW，Clockwise）
    // angular.x 和 angular.y 在2D平面运动中通常为0
    twist_msg.angular.x = 0.0;
    twist_msg.angular.y = 0.0;
    twist_msg.angular.z = current_angular_velocity;

    // 发布Twist消息
    // publish() 将消息发布到之前创建的话题上
    // turtlesim节点会订阅该话题并执行相应的运动
    cmd_vel_pub_->publish(twist_msg);

    // 输出调试信息
    // 每0.5秒输出一次当前状态，避免日志过于频繁
    // static变量只在第一次进入函数时初始化，之后保持上次的值
    static double last_log_time = -1.0;
    if (elapsed_time - last_log_time >= 0.5) {
      last_log_time = elapsed_time;
      RCLCPP_INFO(this->get_logger(),
                  "[t=%.2f s] 发布速度指令: linear.x=%.3f, angular.z=%.3f | 当前阶段: %s",
                  elapsed_time,
                  twist_msg.linear.x,
                  twist_msg.angular.z,
                  (phase < period_) ? "第1个圆 (CCW)" : "第2个圆 (CW)");
    }
  }

  // 成员变量声明
  // 发布者指针：用于向 /turtle1/cmd_vel 话题发布速度指令
  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr cmd_vel_pub_;

  // 定时器指针：以固定频率触发回调函数
  rclcpp::TimerBase::SharedPtr timer_;

  // 启动时间：记录节点启动时刻，用于计算经过的时间
  rclcpp::Time start_time_;

  // 线速度：从参数读取，控制海龟前进速度（m/s）
  double linear_velocity_;

  // 角速度：从参数读取，控制海龟转向速度（rad/s）
  double angular_velocity_;

  // 周期：画一个完整圆所需的时间（s）
  double period_;

  // 控制频率：发布速度指令的频率（Hz）
  int loop_rate_;
};

/**
 * 主函数的工作流程：
 * 1. 调用 rclcpp::init() 初始化ROS2客户端库
 * 2. 创建EightFigureNode节点实例
 * 3. 调用 rclcpp::spin() 进入事件循环，等待回调函数被触发
 * 4. 当节点被关闭（如收到Ctrl+C信号），spin()返回
 * 5. 调用 rclcpp::shutdown() 清理ROS2资源
 * 6. 返回退出码
 */
int main(int argc, char **argv) {
  // 初始化ROS2 C++客户端库
  // 必须在创建任何Node之前调用
  // 该函数会解析命令行参数（如--ros-args等ROS2特定参数）
  rclcpp::init(argc, argv);

  // 创建8字形运动控制节点的共享指针
  // std::make_shared 是C++11引入的智能指针创建方式，比裸指针更安全
  // "eight_figure_node" 是节点的名称，在ROS2网络中唯一标识该节点
  auto node = std::make_shared<EightFigureNode>("eight_figure_node");

  // 进入ROS2事件循环
  // spin() 会阻塞当前线程，持续处理回调函数（如定时器回调、订阅回调等）
  // 直到节点被关闭（例如用户按下Ctrl+C，或者调用rclcpp::shutdown()）
  // spin() 是单线程版本，所有回调都在同一个线程中执行
  rclcpp::spin(node);

  // 清理ROS2资源
  // 释放所有ROS2相关的资源，关闭网络连接
  // 虽然不是严格必须（程序退出时操作系统会回收资源），但良好的实践是显式调用
  rclcpp::shutdown();

  // 返回0表示程序正常退出
  return 0;
}
