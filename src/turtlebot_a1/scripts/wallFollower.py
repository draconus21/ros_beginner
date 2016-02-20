#!/usr/bin/env python

import sys
import numpy as np
import time
import rospy as rp
from geometry_msgs.msg import Twist, Pose
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv  import SetModelState
from sensor_msgs.msg import LaserScan
import matplotlib.pyplot as plt


CMD_VEL             = '/cmd_vel_mux/input/teleop'
SCAN                = '/scan'
SET_MODEL_STATE_SRV = '/gazebo/set_model_state'
BOT                 = 'mobile_base'

DEF_X    = 0
DEF_Y    = 0
Q_SIZE   = 1000
RATE     = 4
N_LASER  = 640
ROT_DIR  = 0.001
FWD_SPD  = 5
C_WIDTH  = 2

ANGULAR_VAL = np.pi/N_LASER
MAX_SIZE    = N_LASER

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
#        print center
        obj_dir = ROT_DIR * 90
    elif np.any(val < min_dist) or val.size<1:
        safe = False
#        print prev_dist
#        print '*' * 20
#        print val_cp
##        print val.shape, val_cp.shape, ANGULAR_VAL
##        print np.where(val == np.min(val)), np.min(val)
        min_laser = np.where(val == np.min(val))[0][0]
        obj_dir = ROT_DIR * (N_LASER/2 - min_laser) * ANGULAR_VAL
#        print 'Not Safe! ', min_laser, ' ', obj_dir
    else:
        safe = True
        obj_dir = 0
#        print val
#        print 'Safe!'
    prev_dist = val_cp
    

def spawnMe(obj=BOT, x=DEF_X, y = DEF_Y):
    mState = ModelState()
    mState.model_name = obj
    
    mState.pose.position.x = x
    mState.pose.position.y = y
    mState.pose.position.z = 0

    mState.pose.orientation.x = 0
    mState.pose.orientation.y = 0
    mState.pose.orientation.z = 0
    mState.pose.orientation.w = 1

    rp.wait_for_service(SET_MODEL_STATE_SRV)

    try:
        sms = rp.ServiceProxy(SET_MODEL_STATE_SRV, SetModelState)
        print 'Spawing:', obj, 'with params', mState
        print sms(mState)
    except rp.ServiceException as e:
        logging.exception('ServiceException while spawning at ' + x + ' ' + y)


def wallFollower(obj=BOT, x=DEF_X, y=DEF_Y):
    rp.init_node('wallFollower')
    
    ## spwan bot at (x, y, 0)
    spawnMe(obj, x, y)

    pub  = rp.Publisher(CMD_VEL, Twist, queue_size=Q_SIZE)
    sub  = rp.Subscriber('/scan', LaserScan, scannerCallback, queue_size=Q_SIZE)
    rate = rp.Rate(RATE)
    vel  = Twist()
    dir  = 1
    np.random.seed(int(time.time()))
    while not rp.is_shutdown():
#        if (np.random.uniform() < 0.5):
#            dir = dir * -1
#        [vel.linear.x, vel.linear.y, vel.linear.z]    = [FWD_SPD, 0, 0]
#        [vel.angular.x, vel.angular.y, vel.angular.z] = [0, 0, 0]
##        print vel
#        if safe == False:
#            vel.linear.x  = 0
#            vel.angular.z = obj_dir * RATE
#            print ' vel: '
#            print vel
#        pub.publish(vel)
        rate.sleep()


if __name__=='__main__':
    try:
        bot = BOT
        x   = DEF_X
        y   = DEF_Y
        if len(sys.argv) == 3:
            x = int(sys.argv[1])
            y = int(sys.argv[2])

        wallFollower(bot, x, y)
    except rp.ROSInterruptException:
        pass
