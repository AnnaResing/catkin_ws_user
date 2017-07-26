#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32

rospy.init_node('ass1', anonymous=True)
pub = rospy.Publisher('/assignment1_publisher_subscriber', String, queue_size=10)


def callback(msg):
   rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)
   pub.publish("I heard %s" % msg.data)


rospy.Subscriber('/model_car/yaw', Float32, callback)
rospy.spin()



