#!/usr/bin/env python

import sys
import rospy

from std_msgs.msg import *
from geometry_msgs.msg import *
from math import *
from tf.transformations import quaternion_from_euler

def talker():
	square_size = rospy.get_param("~square_size", 1.0) 
	# Create a list to hold the target quaternions (orientations)
	quaternions = list()

	# First define the corner orientations as Euler angles
	euler_angles = (pi/2, pi, 3*pi/2, 0)

	# Then convert the angles to quaternions
	for angle in euler_angles:
		q_angle = quaternion_from_euler(0, 0, angle, axes='sxyz')
		q = Quaternion(*q_angle)
		quaternions.append(q)

	# Create a list to hold the waypoint poses
	waypoints = list()

	# Append each of the four waypoints to the list.  Each waypoint
	# is a pose consisting of a position and orientation in the map frame.
	waypoints.append(Pose(Point(square_size, 0.0, 0.0), quaternions[0]))
	waypoints.append(Pose(Point(square_size, square_size, 0.0), quaternions[1]))
	waypoints.append(Pose(Point(0.0, square_size, 0.0), quaternions[2]))
	waypoints.append(Pose(Point(0.0, 0.0, 0.0), quaternions[3]))

	pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)
	rospy.init_node('rbx1_demo', anonymous=True)
	rate = rospy.Rate(1)
	desPos = PoseStamped()
	desPos.header.frame_id='map'
	desPos.header.stamp=rospy.Time.now()
	count = 0
	while not rospy.is_shutdown():


		desPos.pose=waypoints[count]
		count=count+1
		if count < 4:
			count = 0
		#desPos.pose.position.z=0
		#desPos.pose.position.x=10
		#desPos.pose.position.y=count
		#count=count+10
		#if count==100:
		#	count =10
		rospy.loginfo(desPos)
		pub.publish(desPos)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass


