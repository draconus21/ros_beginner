#!/usr/bin/env python

import sys
import numpy as np
import time
import rospy as rp
from geometry_msgs.msg import Twist, Pose
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv  import SetModelState
from sensor_msgs.msg import LaserScan
from bot_basic import *
from constants import *
import matplotlib.pyplot as plt


ROT_DIR  = 0.001
C_WIDTH  = 2

ANG_OFFSET  = 0
MIN_RANGE   = 100
MAX_RANGE   = 0
INC_ANGLE   = 1
MIN_ANLGE   = 100
MAX_ANGLE   = 0
MAX_SIZE    = N_LASER
CENTER      = N_LASER/2

init      = True
safe_dist = np.zeros(MAX_SIZE)
prev_dist = np.zeros(MAX_SIZE)
safe      = False
obj_dir   = 0
min_obj_dist = 1
bot_state = B_CLEAR
wall_side = W_UNKNOWN
wall_dist  = 0

def scannercb2(scan):
    global ANG_OFFSET
    global MIN_RANGE
    global MAX_RANGE
    global INC_ANGLE
    global MIN_ANGLE
    global MAX_ANGLE   
    global safe
    global init
    global bot_state
    global wall_side
    global wall_dist

    if init == True:
        MIN_RANGE  = scan.range_min
        MAX_RANGE  = scan.range_max
        INC_ANGLE  = scan.angle_increment * 180/np.pi
        MIN_ANGLE  = scan.angle_min * 180/np.pi
        MAX_ANGLE  = scan.angle_max * 180/np.pi
        ANG_OFFSET = 90 - MAX_ANGLE
        print MIN_RANGE, MAX_RANGE, INC_ANGLE, MIN_ANGLE, MAX_ANGLE, ANG_OFFSET
        #print scan.header.frame_id
        #print scan.header.angles
        init = False

    ranges = np.array(scan.ranges)
    valid_r = ranges[ranges >= MIN_RANGE]
    valid_r = valid_r[valid_r <= MAX_RANGE]

    if len(valid_r) == 0:
        if wall_side != W_FRONT:
            mvBk()
            return

    min_dist = np.min(valid_r)
    ## Find laser that caused lowest valid range value. Disambiguate
    ## by giving preference to the leftmost laser
    min_las  = np.min(np.where(ranges==min_dist)[0])
    
    #if min_las >= CENTER-C_WIDTH and min_las <= CENTER-C_WIDTH:
    if bot_state == B_CLEAR:
        # safely away from walls, move fwd
        if min_dist > min_obj_dist:
            mvFwd()
        # close to wall (head on), turn right and align with wall
        else:
            angle = 90
            turnA(angle)
            wall_side = W_LEFT
            bot_state = B_WALL_FLW
    if bot_state == B_WALL_FLW:
        if min_dist > min_obj_dist:
            mvFwd()
        else:
            angle = getWallAngle(min_las)
            turnA(angle)

    
    #if min_dist > min_obj_dist:
    #    mvFwd()
    #else:
    #    obj_dir = min_las * INC_ANGLE
    #    if  obj_dir < 0:
    #        turnL(np.abs(obj_dir + ANG_OFFSET))
    #    else:
    #        turnR(np.abs(obj_dir + ANG_OFFSET))
    
    #    print min_dist, min_las, obj_dir
    
def getWallAngle(laser_n):
    diff_angle = (CENTER-laser_n) * INC_ANGLE

    if diff_angle < 0:
        return -ANG_OFFSET + diff_angle
    return ANG_OFFSET + diff_angle

def turn(turn_angle):
    pub = rp.Publisher(CMD_VEL, Twist, queue_size=Q_SIZE)
    
    rate = rp.Rate(RATE)
    vel  = Twist()

    if turn_angle == 0:
        vel.linear.x = FWD_SPD
    else:
        vel.linear.x = 0
    vel.linear.y = 0
    vel.linear.z = 0

    vel.angular.x = 0
    vel.angular.y = 0
    if turn_angle > 0:
        vel.angular.z = 1
    else:
        vel.angular.z = -1

    pub.publish(vel)
    rate.sleep()

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
    

#def spawnMe(obj=BOT, x=DEF_X, y = DEF_Y):
#    mState = ModelState()
#    mState.model_name = obj
#    
#    mState.pose.position.x = x
#    mState.pose.position.y = y
#    mState.pose.position.z = 0
#
#    mState.pose.orientation.x = 0
#    mState.pose.orientation.y = 0
#    mState.pose.orientation.z = 0
#    mState.pose.orientation.w = 1
#
#    rp.wait_for_service(SET_MODEL_STATE)
#
#    try:
#        sms = rp.ServiceProxy(SET_MODEL_STATE, SetModelState)
#        #print 'Spawing:', obj, 'with params', mState
#        #print sms(mState)
#    except rp.ServiceException as e:
#        logging.exception('ServiceException while spawning at ' + x + ' ' + y)


def wallFollower(obj=BOT, x=DEF_X, y=DEF_Y):
    rp.init_node('wallFollower')
    
    ## spwan bot at (x, y, 0)
    spawnMBase(x, y)

    #pub  = rp.Publisher(CMD_VEL, Twist, queue_size=Q_SIZE)
    sub  = rp.Subscriber('/scan', LaserScan, scannercb2, queue_size=Q_SIZE)
    rate = rp.Rate(RATE)
    #vel  = Twist()
    #dir  = 1
    #np.random.seed(int(time.time()))
    while not rp.is_shutdown():
    #    if (np.random.uniform() < 0.5):
    #        dir = dir * -1
    #    [vel.linear.x, vel.linear.y, vel.linear.z]    = [FWD_SPD, 0, 0]
    #    [vel.angular.x, vel.angular.y, vel.angular.z] = [0, 0, 0]
    #    #print vel
    #    if safe == False:
    #        vel.linear.x  = 0
    #        vel.angular.z = obj_dir * RATE
    #        #print ' vel: '
    #        #print vel
    #    pub.publish(vel)
        rate.sleep()


if __name__=='__main__':
    try:
        bot = BOT
        x   = DEF_X
        y   = DEF_Y
        if len(sys.argv) == 3:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
        #spawnMBase()
        wallFollower(bot, x, y)
    except rp.ROSInterruptException:
        pass
