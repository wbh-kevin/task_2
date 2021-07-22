#!/usr/bin/env python 

import roslib
roslib.load_manifest('learning_tf')
import rospy
import tf
import pandas as pd
import numpy as np
import time
import math
from nav_msgs.msg import Odometry
from rospy.core import rospyinfo
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist, Quaternion
from tf.transformations import quaternion_from_euler

if __name__ == '__main__':
	rospy.init_node ('tf_broadcaster')
	#df= pd.read_excel('table1.xlsx') #reading file
	df = pd.read_excel(r'~/catkin_ws/src/learning_tf/nodes/table1.xlsx')
	t = 1
	a = 0.1
	b = 0.1
	r = 0.05
	while( rospy.is_shutdown() ):
		msg = geometry_msgs.msg.Twist()
		vx = ( 0 - df.ix[t][2] + df.ix[t][3] + df.ix[t][4] - df.ix[t][5] )/ 4
		vy = ( 0 - df.ix[t][2] - df.ix[t][3] + df.ix[t][4] + df.ix[t][5] )/ 4
		vx = ( 0 - df.ix[t][2] - df.ix[t][3] - df.ix[t][4] - df.ix[t][5] )/( 4 * a + 4 * b )
		msg.linear.x = vx
		msg.linear.y = vy
		msg.angular.z = vw
		t += 1
		pub = rospy.Publisher( 'tf_broadcaster/tf', Twist, queue_size = 10)
		rospy.spin()
