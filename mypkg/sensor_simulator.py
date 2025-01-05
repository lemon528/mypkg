# SPDX-FileCopyrightText: 2025 Kouhei Kobayashi
# SPDX-License-Identifire: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math


class SensorSimulator(Node):
    def __init__(self):
        super().__init__("sensor_simulator")
        self.publisher = self.create_publisher(Float32, "sensor_data", 10)
        self.step = 0
        self.create_timer(2.0, self.publish_sensor_data)


    def publish_sensor_data(self):
        self.step += 1
        base_value = 5.0 + 2.0 * math.sin(self.step * 0.5)

        msg = Float32()
        msg.data = base_value
        self.publisher.publish(msg)


def main():
    rclpy.init()
    node = SensorSimulator()
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
