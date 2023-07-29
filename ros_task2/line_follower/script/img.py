#!/usr/bin/env python3


import rospy
import cv2

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class camera_1:

  def __init__(self):
    self.image_sub = rospy.Subscriber("/rrbot/camera1/image_raw", Image, self.callback)

  def callback(self,data):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="bgr8")
    # cv_image=cv_image[790:791,170:620]
    # gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    # _, binary_image = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
    # image = cv_image[530:790,165:635]
    # cv2.imshow("ROBOT_CAM2", binary_image)
    
    
    cv2.imshow("ROBOT_CAM", cv_image)
    cv2.waitKey(3)
    

if __name__ == '__main__':
    rospy.init_node('camera_read', anonymous=False)
    camera_1()
    rospy.spin()
    

    

    



  
  
  
 
  

