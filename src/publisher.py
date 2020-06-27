import rospy
from geometry_msgs.msg import Twist
rospy.init_node("test")
speed = Twist()
speed.linear.x = 0
speed.angular.z = 0.3
pub = rospy.Publisher("/cmd_vel",Twist)
while not rospy.is_shutdown():
    pub.publish(speed)