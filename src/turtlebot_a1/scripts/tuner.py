#!/usr/bin/env python

import sys
import time
import numpy as np
import time
import rospy as rp
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
nan = np.nan
stop = False
init = True

def_val = 0

def callback(scan):
    global stop
    global def_val
    global init    
    
    val = np.array(scan.ranges)
    #val = val[~np.isnan(val)]
    if init == True:
        def_val = val

    diff = val-def_val
    diff = np.sum(diff[~np.isnan(diff)])
    print diff
    if diff == 0.0 and not init:
        stop = True
    init = False
    #stop = np.equal(val, def_val)

def tuner():
    rp.init_node('tuner')

    pub = rp.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=1000)
    sub = rp.Subscriber('/scan', LaserScan, callback, queue_size=1000)

    rate = rp.Rate(4)
    vel  = Twist()
    t = time.time()

    while not rp.is_shutdown():
        #if stop:
        #    break
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0

        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0.5

#        print 'start:', t, stop
        pub.publish(vel)
        if stop:
            break
    stop_t = time.time()
    print 'stop_t:', stop_t
    print 'exec time:', (stop_t-t)
    rp.signal_shutdown('got it'+str(stop_t-t))

if __name__=='__main__':
    tuner()

