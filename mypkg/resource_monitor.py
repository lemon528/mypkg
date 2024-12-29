import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil

class ResourceMonitorNode(Node):
    def __init__(self):
        super().__init__("resource_monitor")
        self.publisher = self.create_publisher(String, "system_resources", 10)
        self.create_timer(1.0, self.publish_resources)
        self.get_logger().info("ResourceMonitorNode is running...")


    def publish_resources(self):
        cpu_usage = psutil.cpu_percent(interval=None)
        memory = psutil.virtual_memory()
        msg = String()
        msg.data = (
                f"CPU usage: {cpu_usage}%, "
                f"Memory usage: {memory.percent}%"
        )
        self.publisher.publish(msg)
        self.get_logger().info(msg.data)


def main():
    rclpy.init()
    node = ResourceMonitorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
