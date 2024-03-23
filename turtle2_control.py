import rclpy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def keyboard_control():
    rclpy.init()
    node = rclpy.create_node('keyboard_control')
    publisher = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
    msg = Twist()

    while rclpy.ok():
        key = input("Use arrow keys to move the turtle. Press 'q' to quit: ")
        if key == 'q':
            break
        if key == 'w':
            msg.linear.x = 1.0
        elif key == 's':
            msg.linear.x = -1.0
        elif key == 'a':
            msg.angular.z = 1.0
        elif key == 'd':
            msg.angular.z = -1.0
        publisher.publish(msg)
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    keyboard_control()
