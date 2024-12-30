import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math
import time


class NoisySensorSimulator(Node):
    def __init__(self):
        super().__init__("noisy_sensor_simulator")
        self.publisher = self.create_publisher(Float32, "noisy_sensor_data", 10)
        self.start_time = time.time()
        self.create_timer(1.0, self.publish_sensor_data)


    def publish_sensor_data(self):
        current_time = time.time() - self.start_time
        base_value = 5.0 + 2.0 * math.sin(current_time)
        noise = math.sin(current_time * 5) * 0.2
        sensor_value = base_value + noise

        msg = Float32()
        msg.data = sensor_value
        self.publisher.publish(msg)
        self.get_logger().info(f"Noisy Sensor value: {sensor_value:.2f}")


def main():
    rclpy.init()
    node = NoisySensorSimulator()
    try:
        rclpy.spin(node)
    except rclpy.executors.ExternalShutdownException:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()



if __name__ == "__main__":
    main()
