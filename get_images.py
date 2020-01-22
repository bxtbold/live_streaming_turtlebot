#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image

def img_callback(msg):		# receives and stores the images 
	pass

rospy.init_node('get_images')		# creating a node and naming it get_images

subscribing = rospy.Subscriber('/camera/depth/image_raw',Image, img_callback)	# subscribing images from the camera

rospy.spin()
