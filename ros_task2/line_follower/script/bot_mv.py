#!/usr/bin/env python3
 
        
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2
import numpy as np

class LineFollowerBot:
    def __init__(self):
        rospy.init_node('line_follower_bot', anonymous=True)
        self.bridge = CvBridge()
        self.image_subscriber = rospy.Subscriber('/rrbot/camera1/image_raw', Image, self.image_callback)
        self.cmd_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=3)
        self.kp = 0.1  # Proportional gain .1
        self.ki = 0.00001 # Integral gain .0001
        self.kd = 0.0 # Derivative gain
        
        self.prev_error = 0
        self.integral = 0

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        
        self.process_image(cv_image)
        
        

    def process_image(self, cv_image):
        cv_image=cv_image[790:791,170:620]
        gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        
        _, binary_image = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
        line_position = np.argmin(binary_image,axis=1)

        center = cv_image.shape[1] // 2
        error = int(line_position)+53 - center 
        # Set the linear and angular velocities based on the error 
        linear_vel = 0.5  
        angular_vel = self.update(error) 

        # Publish the Twist message to move the bot
        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = linear_vel
        cmd_vel_msg.angular.z = angular_vel
        self.cmd_vel_publisher.publish(cmd_vel_msg)
        
        
        

        

    
        

    def update(self, error):
        
        self.integral += error
        derivative = error - self.prev_error
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.prev_error = error
        return output    



    def stop(self):
        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = 0
        cmd_vel_msg.angular.z = 0
        self.cmd_vel_publisher.publish(cmd_vel_msg)    

if __name__ == '__main__':
    try:
        line_follower_bot = LineFollowerBot()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

    finally:
        line_follower_bot.stop()
           
