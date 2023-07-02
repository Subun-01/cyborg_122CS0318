#!/usr/bin/env python3


import rospy
# import turtle
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose



class main:
    def __init__(self):
        rospy.init_node("turtle_move",anonymous=True)
        self.pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
        self.rate= rospy.Rate(50)
        self.sub_pos=rospy.Subscriber("/turtle1/pose",Pose,self.callback)
        self.pos=Pose()
        self.msg=Twist()

    def callback(self,msg1):
        self.pos=msg1
        # self.pos.x=round(self.pos.x,7)
        # self.pos.y=round(self.pos.y,7)

    def curve_D(self):
        self.msg.linear.x=3.14159265359
        self.msg.angular.z=-3.14159265359
        self.pub.publish(self.msg)
        self.rate.sleep()
        

    def straight_D(self):
        self.msg.linear.y=.3
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
            if(t.pos_x()==5.544444561004639):
                
                if(t.pos_y()<7.54444456100464):
                    t.straight_D()
                    rospy.loginfo("My turtle is: moving in straightline")
                    
        
                elif(t.pos_y()>=7.54444456100464): 
                    t.curve_D()
                    rospy.loginfo("My turtle is: moving in curve")
                    
            else:
                rospy.loginfo("My turtle is: not moving")

            rospy.loginfo('position: ['+str(t.pos_x())+'] ['+str(t.pos_y())+']')        
            rospy.loginfo('orientation: ['+str(t.pos_o())+']')   
             
            
            
            
               
        except rospy.ROSInterruptException:
            pass

        
        
            
