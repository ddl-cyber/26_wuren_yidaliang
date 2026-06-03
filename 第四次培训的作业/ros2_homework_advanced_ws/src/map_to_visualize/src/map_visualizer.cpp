/**
 * 功能说明：
 *   订阅 /estimation/slam/map 话题（消息类型 fsd_common_msgs::msg::Map），
 *   将地图中的各色锥桶（黄色/蓝色/红色/未知）转换为 visualization_msgs::msg::MarkerArray，
 *   发布到 /cone_markers 话题，供 rviz2 订阅并可视化显示。
 *
 * 坐标系说明（重要）：
 *   bag 文件中 Map 消息的 header.frame_id 为 "world"。
 *   rviz2 默认的 Fixed Frame 通常是 "map"，两者名称不一致。
 */

#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "visualization_msgs/msg/marker_array.hpp"
#include "fsd_common_msgs/msg/map.hpp"
#include "fsd_common_msgs/msg/cone.hpp"

// std::placeholders::_1 用于 std::bind，将回调的第一个参数绑定为收到的消息指针
using std::placeholders::_1;

/**
 * ROS 2 节点生命周期：
 *   1. rclcpp::init() 初始化 ROS 2 客户端库（main 中完成）；
 *   2. 创建 Node 实例，此时节点名称注册到 ROS 2 图（Graph）中；
 *   3. 创建 Subscription 和 Publisher，建立话题连接；
 *   4. rclcpp::spin() 进入事件循环，等待并处理回调；
 *   5. rclcpp::shutdown() 关闭，释放资源。
 */
class MapVisualizer : public rclcpp::Node
{
public:
    /**
     *   调用父类构造函数，节点名称为 "map_visualizer"。
     *   在构造函数中完成话题的创建，这是 ROS 2 的常用模式（RAII）。
     */
    MapVisualizer() : Node("map_visualizer")
    {
        // 创建订阅者，订阅 /estimation/slam/map 话题，消息类型为 fsd_common_msgs::msg::Map。
        // QoS (Quality of Service) 深度设为 10，即队列最多缓存 10 条消息。
        // 对于 bag 播放这种低频、可靠传输的场景，QoS 深度 10 足够。
        // std::bind 将成员函数 map_callback 与 this 指针绑定，_1 占位符表示消息参数。
        map_sub_ = this->create_subscription<fsd_common_msgs::msg::Map>(
            "/estimation/slam/map", 10,
            std::bind(&MapVisualizer::map_callback, this, _1));

        // 创建发布者，发布 /cone_markers 话题，rviz2 通过订阅此话题获取可视化对象。
        marker_pub_ = this->create_publisher<visualization_msgs::msg::MarkerArray>(
            "/cone_markers", 10);

        RCLCPP_INFO(this->get_logger(),
            "MapVisualizer 节点已启动，等待 /estimation/slam/map 话题数据...");
        RCLCPP_INFO(this->get_logger(),
            "提示：请在 rviz2 中将 Fixed Frame 设置为 'world'，与 bag 文件的坐标系保持一致。");
    }

private:
    /**
     * 回调触发时机：
     *   当 ros2 bag play 开始发布 /estimation/slam/map 消息后，ROS 2 中间层会调用此函数，将反序列化后的消息对象传入。
     *
     * 处理流程：
     *   1. 读取坐标系 frame_id；
     *   2. 遍历四种颜色的锥桶数组，分别生成对应颜色的 Sphere Marker（设置 lifetime 自动过期）；
     *   3. 将新生成的 MarkerArray 发布出去。
     */
    void map_callback(const fsd_common_msgs::msg::Map::SharedPtr msg)
    {
        // 读取坐标系 frame_id
        // Map.msg 的 std_msgs/Header 中包含 frame_id，描述的是该地图数据所在的坐标系。
        // 通过查看 bag 文件可知，此处的 frame_id 实际为 "world"。
        std::string frame_id = msg->header.frame_id;

        /* ---------- 旧 Marker 清理策略说明（非执行步骤，仅注释说明） ---------- */
        // 本代码采用 lifetime（生命周期）机制自动清理旧 Marker，而非 DELETEALL 方式。
        // 两种清理旧 Marker 的策略对比：
        //
        // 策略 A: DELETEALL（已注释掉，保留供参考）
        //   在每帧开始时，对每个命名空间发送 action=DELETEALL 的 Marker，lifetime=0.0。
        //   rviz 收到后会删除该 ns 下的所有 Marker，然后再发送新 Marker 覆盖。
        //   缺点：会出现闪烁
        //
        // 策略 B: lifetime 自动过期（当前采用）
        //   将每个 Marker 的 lifetime 设为较短值（本代码为 0.15 秒），
        //   rviz 内部计时器到期后自动删除该 Marker，无需手动发送删除指令。
        //   优点：代码简洁，无乱序风险，天然处理动态增减的锥桶。
        //        本 bag 的发布频率约 10Hz，lifetime=0.15s 足够覆盖两帧间隔。
        //
        // 以下是 DELETEALL 方式的参考实现，保留在此方便理解和对比：
        //
        // visualization_msgs::msg::MarkerArray delete_marks;
        // for (const auto & ns : {"cone_yellow", "cone_blue", "cone_red", "cone_unknown"})
        // {
        //     visualization_msgs::msg::Marker del;
        //     del.header.frame_id = frame_id;
        //     del.header.stamp = this->now();
        //     del.ns = ns;
        //     del.action = visualization_msgs::msg::Marker::DELETEALL;
        //     delete_marks.markers.push_back(del);
        // }
        // marker_pub_->publish(delete_marks);

        // 生成 MarkerArray
        visualization_msgs::msg::MarkerArray marker_array;
        int id_counter = 0;  // 同一命名空间下，Marker ID 必须唯一

        // 依次处理黄色、蓝色、红色、未知四种锥桶
        // Map.msg 定义了四个数组：cone_yellow, cone_blue, cone_red, cone_unknown
        for (const auto & cone : msg->cone_yellow)
        {
            auto marker = make_cone_marker(frame_id, cone, "yellow", id_counter++);
            marker_array.markers.push_back(marker);
        }
        for (const auto & cone : msg->cone_blue)
        {
            auto marker = make_cone_marker(frame_id, cone, "blue", id_counter++);
            marker_array.markers.push_back(marker);
        }
        for (const auto & cone : msg->cone_red)
        {
            auto marker = make_cone_marker(frame_id, cone, "red", id_counter++);
            marker_array.markers.push_back(marker);
        }
        for (const auto & cone : msg->cone_unknown)
        {
            auto marker = make_cone_marker(frame_id, cone, "unknown", id_counter++);
            marker_array.markers.push_back(marker);
        }

        // 发布 MarkerArray
        // 将本次生成的所有 Marker 一次性发布，rviz2 收到后会立即更新显示。
        marker_pub_->publish(marker_array);

        // 打印日志，方便在终端观察数据是否流动、锥桶数量是否正确。
        RCLCPP_INFO(this->get_logger(),
            "已发布锥桶 | 黄:%zu 蓝:%zu 红:%zu 未知:%zu | frame_id: %s",
            msg->cone_yellow.size(), msg->cone_blue.size(),
            msg->cone_red.size(), msg->cone_unknown.size(),
            frame_id.c_str());
    }

    /**
     * Marker 类型说明：
     *   visualization_msgs::msg::Marker::SPHERE 表示球体，适合近似表示锥桶。
     *   其他常用类型：CUBE（立方体）、CYLINDER（圆柱体）、ARROW（箭头）、TEXT_VIEW_FACING（文字）等。
     *
     * 颜色与命名空间映射：
     *   "yellow" -> 黄色 (1,1,0)   ns="cone_yellow"
     *   "blue"   -> 蓝色 (0,0,1)   ns="cone_blue"
     *   "red"    -> 红色 (1,0,0)   ns="cone_red"
     *   "unknown"-> 灰色 (0.5,0.5,0.5) ns="cone_unknown"
     *
     * 命名空间（ns）的作用：
     *   rviz2 允许按命名空间筛选/显隐 Marker。把不同颜色的锥桶放在不同 ns 下，
     *   可以在 rviz 的 Displays 面板中单独勾选/取消某种颜色的显示，方便调试。
     */
    visualization_msgs::msg::Marker make_cone_marker(
        const std::string & frame_id,
        const fsd_common_msgs::msg::Cone & cone,
        const std::string & color_str,
        int id)
    {
        visualization_msgs::msg::Marker marker;

        // Header: frame_id 决定 Marker 在哪个坐标系下绘制；stamp 决定时间戳。
        marker.header.frame_id = frame_id;
        marker.header.stamp = this->now();

        // ns (namespace) + id 共同构成 Marker 的全局唯一标识。
        // rviz 中同一个 ns:id 组合的 Marker 会被覆盖更新（即"原地更新"机制）。
        marker.ns = "cone_" + color_str;
        marker.id = id;

        // 几何类型与动作
        marker.type = visualization_msgs::msg::Marker::SPHERE;
        marker.action = visualization_msgs::msg::Marker::ADD;  // ADD 表示新增或更新

        // 位置：直接读取 Cone 消息中的 geometry_msgs/Point
        marker.pose.position.x = cone.position.x;
        marker.pose.position.y = cone.position.y;
        marker.pose.position.z = cone.position.z;
        marker.pose.orientation.w = 1.0;  // 单位四元数，表示无旋转

        // 尺寸：scale 表示球体在 x/y/z 三个方向的直径（单位：米）。
        // 这里统一设为 0.3m，约等于真实锥桶的底面直径，可在 rviz 中根据观感微调。
        marker.scale.x = 0.3;
        marker.scale.y = 0.3;
        marker.scale.z = 0.3;

        // lifetime: Marker 在 rviz 中的存活时间（从收到 Marker 消息的时刻开始计时）。
        // 设为 0.15 秒：既足够让相邻两帧之间不出现闪烁（本 bag 约 10Hz，帧间隔 ~0.1s），
        // 又能在锥桶从地图中消失后迅速将其移除，避免残留"重影"。
        // 这是策略 B（lifetime 自动过期）的核心参数，详见 Step 2 注释中的策略对比。
        // 若设为 0.0 表示永久显示，需配合 DELETEALL 手动清理（旧策略，会闪烁）。
        marker.lifetime = rclcpp::Duration::from_seconds(0.15);

        // RGBA 颜色设置，a (alpha) = 1.0 表示完全不透明
        if (color_str == "yellow") {
            marker.color.r = 1.0f;
            marker.color.g = 1.0f;
            marker.color.b = 0.0f;
            marker.color.a = 1.0f;
        } else if (color_str == "blue") {
            marker.color.r = 0.0f;
            marker.color.g = 0.0f;
            marker.color.b = 1.0f;
            marker.color.a = 1.0f;
        } else if (color_str == "red") {
            marker.color.r = 1.0f;
            marker.color.g = 0.0f;
            marker.color.b = 0.0f;
            marker.color.a = 1.0f;
        } else {  // "unknown" 或兜底情况
            marker.color.r = 0.5f;
            marker.color.g = 0.5f;
            marker.color.b = 0.5f;
            marker.color.a = 1.0f;
        }

        return marker;
    }

    // 成员变量：订阅者和发布者的共享指针
    // SharedPtr 采用引用计数机制，当 MapVisualizer 对象析构时自动释放资源
    rclcpp::Subscription<fsd_common_msgs::msg::Map>::SharedPtr map_sub_;
    rclcpp::Publisher<visualization_msgs::msg::MarkerArray>::SharedPtr marker_pub_;
};

/**
 * 标准流程：
 *   1. rclcpp::init(argc, argv) 解析命令行参数并初始化 rclcpp；
 *   2. 创建节点实例（std::make_shared<MapVisualizer>()）；
 *   3. rclcpp::spin(node) 阻塞当前线程，进入事件循环，处理订阅回调、定时器、服务请求等；
 *   4. 当用户按下 Ctrl+C 时，spin 返回，执行 rclcpp::shutdown() 清理资源；
 *   5. return 0 正常退出。
 */
int main(int argc, char ** argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MapVisualizer>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
