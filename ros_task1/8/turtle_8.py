#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose



class main:
    def __init__(self):
        rospy.init_node("turtle_move",anonymous=True)
        self.pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
        self.rate= rospy.Rate(10)
        self.sub_pos=rospy.Subscriber("/turtle1/pose",Pose,self.callback)
        self.pos=Pose()
        self.msg=Twist()

    def callback(self,msg1):
        self.pos=msg1
        
    def curve_D(self):
        self.msg.linear.x=1.0
        self.msg.angular.z=1.0
        self.pub.publish(self.msg)
        self.rate.sleep()
        
    def curve8(self):
        self.msg.linear.x=1.0
        self.msg.angular.z=-1.0
        self.pub.publish(self.msg)
        self.rate.sleep()

    def stop(self):
        self.msg.linear.x=0.0
        self.msg.angular.z=0.0
        self.pub.publish(self.msg)
        self.rate.sleep()
        
    def pos_x(self):
        return self.pos.x
    
    def pos_y(self):
        return self.pos.y
    
    def pos_o(self):
        return self.pos.theta


if __name__=='__main__':
    i=1
    t=main()
    
    
    while not rospy.is_shutdown():
        
        
        try:
            
            if(i<=10 and t.pos_x()==5.544444561004639 and t.pos_y()==5.544444561004639):
                t.curve_D()
                rospy.loginfo("My turtle is: moving in curve")
                i=i+1
            elif(round(t.pos_y(),2)>5.54):
                t.curve_D()
                rospy.loginfo("My turtle is: moving in curve")
                i=i+1
            elif(round(t.pos_y(),2)<5.54):  
                t.curve8()
                rospy.loginfo("My turtle is: moving in curve")
                i=i+1
            elif(i>40 and round(t.pos_x())==6 and round(t.pos_y())==6):
                t.curve8()
                rospy.loginfo("My turtle is: moving in curve")
                i=i+1    
            elif(i>100 and round(t.pos_y(),1)==5.5 and round(t.pos_x(),1)==5.5):
                t.stop()
                rospy.loginfo("My turtle is: not moving")
                
            rospy.loginfo('position: ['+str(t.pos_x())+'] ['+str(t.pos_y())+']')        
            rospy.loginfo('orientation: ['+str(t.pos_o())+']')
               
                    
             
            
            
            
               
        except rospy.ROSInterruptException:
            pass