#!/usr/bin/env python

import numpy as np
import time
import rospy as rp
from geometry_msgs.msg import Twist, Pose
from sensor_msgs.msg import LaserScan
import matplotlib.pyplot as plt

Q_SIZE   = 1000
RATE     = 4
N_LASER  = 640
MAX_SIZE = N_LASER
ROT_DIR  = 0.001
FWD_SPD  = 5
ANGULAR_VAL = np.pi/N_LASER
C_WIDTH  = 2

safe_dist = np.zeros(MAX_SIZE)
prev_dist = np.zeros(MAX_SIZE)
safe      = False
obj_dir   = 0

def scannerCallback(scan):
    global safe_dist
    global prev_dist
    global obj_dir
    global safe

    val = np.array(scan.ranges)
    for i in range(MAX_SIZE):
        if np.isnan(val[i]) and not np.isnan(prev_dist[i]):
            safe_dist[i] = prev_dist[i]
    val_cp = val
    val    = val[~np.isnan(val)]
    center = val_cp[N_LASER/2-C_WIDTH:N_LASER/2+C_WIDTH]

    min_dist = np.max(safe_dist)
    
    if np.any(np.isnan(center)):
        safe = False
        print center
        obj_dir = ROT_DIR * 90
    elif np.any(val < min_dist) or val.size<1:
        safe = False
        print prev_dist
        print '*' * 20
        print val_cp
#        print val.shape, val_cp.shape, ANGULAR_VAL
#        print np.where(val == np.min(val)), np.min(val)
        min_laser = np.where(val == np.min(val))[0][0]
        obj_dir = ROT_DIR * (N_LASER/2 - min_laser) * ANGULAR_VAL
        print 'Not Safe! ', min_laser, ' ', obj_dir
    else:
        safe = True
        obj_dir = 0
#        print val
        print 'Safe!'
    prev_dist = val_cp
    

def wallFollower():
    rp.init_node('wallFollower')
    
    pub  = rp.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=Q_SIZE)
    sub  = rp.Subscriber('/scan', LaserScan, scannerCallback, queue_size=Q_SIZE)
    rate = rp.Rate(RATE)
    vel  = Twist()
    dir  = 1
    np.random.seed(int(time.time()))
    while not rp.is_shutdown():
        if (np.random.uniform() < 0.5):
            dir = dir * -1
        [vel.linear.x, vel.linear.y, vel.linear.z]    = [FWD_SPD, 0, 0]
        [vel.angular.x, vel.angular.y, vel.angular.z] = [0, 0, 0]
#        print vel
        if safe == False:
            vel.linear.x  = 0
            vel.angular.z = obj_dir * RATE
            print ' vel: '
            print vel
        pub.publish(vel)
        rate.sleep()


if __name__=='__main__':
    try:
        wallFollower()
    except rp.ROSInterruptException:
        pass
