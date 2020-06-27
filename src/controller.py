#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point,Twist
from math import atan2

x = 0.0
y = 0.0
theta = 0.0
rospy.init_node("go_to_goal")
def newOdom(msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    rot_q = msg.pose.pose.orientation
    (roll,pitch,theta) = euler_from_quaternion([rot_q.x,rot_q.y,rot_q.z,rot_q.w])
    #rospy.loginfo(theta)


goal = Point()
r = rospy.Rate(5)
goal.x = 10
goal.y = 10
speed = Twist()

sub = rospy.Subscriber("/odom",Odometry,newOdom)
pub = rospy.Publisher("/cmd_vel",Twist)
while not rospy.is_shutdown():
    inc_x = goal.x - x
    inc_y = goal.y - y
    angle_to_goal = atan2(inc_x,inc_y)
    rospy.loginfo(inc_x)
    if(abs(angle_to_goal-theta))>0.15:
     speed.linear.x = 0.0
     speed.angular.z = 0.3
    else:
     speed.linear.x = 0.2
     speed.angular.z = 0.0
    if(abs(inc_x)<2.5 and  abs(inc_y)<2.5):
            speed.linear.x = 0
            speed.angular.z =0

   # print("publishing speed ....")
    pub.publish(speed)
    r.sleep()
