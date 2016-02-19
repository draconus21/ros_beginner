#!/usr/bin/env python

import sys
import numpy as np
import random
import time
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

closeToObst   = 0
action_dur    = 4
mvt_speed     = 0.25
turn_speed    = 0.5
min_turn_dur  = 3
max_turn_dur  = 10
min_wall_dist = 0

prev_dist_l   = 0
prev_dist_c   = 0
prev_dist_r   = 0

def scannerCallback (scan):
    global prev_dist_l
    global prev_dist_c
    global prev_dist_r
    global min_wall_dist
    global closeToObst

    a = scan.ranges
    center = int(len(a)/2)
    #rospy.loginfo(rospy.get_caller_id() + ' Range in front = %f', a[int(len(a)/2)])
    if np.isnan(a[0]) and not np.isnan(prev_dist_l):
       print 'max allowed distance_l: ', min_wall_dist, ' ', prev_dist_l, ' ', a[0]
       min_wall_dist = np.max([prev_dist_l, min_wall_dist])
#       rospy.signal_shutdown('got NaN from Laser')
    
    if np.isnan(a[center]) and not np.isnan(prev_dist_c):
       print 'max allowed distance_c: ', min_wall_dist, ' ', prev_dist_c, ' ', a[center]
       min_wall_dist = np.max([prev_dist_c, min_wall_dist]) 
#       rospy.signal_shutdown('got NaN from Laser')
 
    if np.isnan(a[-1]) and not np.isnan(prev_dist_r):
       print 'max allowed distance_r: ', min_wall_dist, ' ', prev_dist_r, ' ', a[-1]
       min_wall_dist = np.max([prev_dist_r, min_wall_dist]) 
#       rospy.signal_shutdown('got NaN from Laser')
   
    if (a[0] <= min_wall_dist) or (a[center] <= min_wall_dist) or (a[-1] <= min_wall_dist):
       closeToObst = 1
    else:
        print '[', a[0], ' ', a[center], ' ', a[-1], ']'
        closeToObst = 0

#    if np.any(np.isnan(a)):
#        print 'NaNs at: '
#        print np.where(np.isnan(a))

    prev_dist_l = a[0]
    prev_dist_c = a[center]
    prev_dist_r = a[-1]

def random_duration():
    random.seed(rospy.get_rostime().nsecs)
    dur = random.randrange(min_turn_dur, max_turn_dur)
    rospy.loginfo(rospy.get_caller_id() + ' Rand dur: %f', dur)
    return dur/10

def turn(cmd_pub, duration, turn_speed):
    vel = Twist()
    stopTime = rospy.get_time() + duration
    print stopTime, ' ', rospy.get_time(), rospy.get_rostime()
    rate = rospy.Rate(action_dur)
    while rospy.get_time() < stopTime:
#        rospy.loginfo(rospy.get_caller_id() + " Turning for %f seconds", duration)
        vel.linear.x = 0.0
        vel.linear.y = 0.0
        vel.linear.z = 0.0

        vel.angular.x = 0.0
        vel.angular.y = 0.0
        vel.angular.z = turn_speed

        cmd_pub.publish(vel)
        rate.sleep()

def randomWalk():
    rospy.init_node('randomWalk')
    cmd_pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=1000)
    sub     = rospy.Subscriber('/scan', LaserScan, scannerCallback, queue_size=1000)

    vel = Twist()
    rate = rospy.Rate(action_dur)
    while not rospy.is_shutdown():
        if closeToObst == 1:
#            rospy.loginfo('Very Clost to Obstacle. Turning for a random duration.')
            dur = random_duration()
            turn(cmd_pub, dur, turn_speed)
        else:
#            rospy.loginfo('Moving straight ahead.')
            vel.linear.x = mvt_speed
            vel.linear.y = 0.0
            vel.linear.z = 0.0
            
            vel.angular.x = 0.0
            vel.angular.y = 0.0
            vel.angular.z = 0.0
            cmd_pub.publish(vel)
        rate.sleep()


if __name__ == '__main__':
    try:
        #prev_dist = 1000
        randomWalk()
    except rospy.ROSInterruptException:
        pass
