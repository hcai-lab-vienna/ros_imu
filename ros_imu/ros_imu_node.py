#!/usr/bin/env python3

import serial

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu


class IMUNode(Node):
    def __init__(self):
        super().__init__('imu_node')
        self.serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.imu_pub = self.create_publisher(Imu, '/imu', 10)
        self.timer = self.create_timer(0.05, self.read_serial)

    def read_serial(self):
        if self.serial_port.in_waiting:
            line = self.serial_port.readline().decode('utf-8').strip()
            data = line.split(',')
            accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z, = map(float, data)
            imu_msg = Imu()
            imu_msg.header.stamp = self.get_clock().now().to_msg()
            imu_msg.linear_acceleration.x = accel_x
            imu_msg.linear_acceleration.y = accel_y
            imu_msg.linear_acceleration.z = accel_z
            imu_msg.angular_velocity.x = gyro_x
            imu_msg.angular_velocity.y = gyro_y
            imu_msg.angular_velocity.z = gyro_z
            self.imu_pub.publish(imu_msg)


def main(args=None):
    rclpy.init(args=args)
    node = IMUNode()
    rclpy.spin(node)
    node.serial_port.close()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
