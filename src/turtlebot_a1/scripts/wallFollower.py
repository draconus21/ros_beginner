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
INC_ANGLE   = 60.0/640
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
bot_state = B_UNKNOWN
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

    print 'bs:', bot_state
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
    
    cen_dist = ranges[CENTER]
    
#    if bot_state == B_UNKNOWN:
#        print 'bot state unknown'
#        mvFwd()
#        bot_state = B_FWD
#        return

##    if np.isnan(cen_dist):
##        print 'cen is nan...b_state:', bot_state, ' ',
##        if bot_state == B_UNKNOWN:
##            print 'too close...moving fwd'
##            mvFwd()
##            bot_state = B_FWD
##        if bot_state == B_FWD:
#            print 'too close...moving back'
#            mvBk()
#            bot_state = B_BK
#        elif bot_state == B_BK:
#            print 'too close...moving fwd'
#            mvFwd()
#            bot_state = B_FWD
#        elif bot_state == B_LEFT:
#            print 'too close...turning right'
#            turnR()
#            mvFwd()
#            bot_state = B_FWD
#        elif bot_state == B_RIGHT:
#            print 'too close...turning left'
#            turnL()
#            mvFwd()
#            bot_state = B_FWD
#        else:
#            print 'not doing anything. state:', bot_state
#        return

    if len(valid_r) == 0:
        #if wall_side != W_FRONT:
        if bot_state == B_BK:
            print 'all ranges are nan...move back'
            mvBk()
            bot_state = B_BK
        else:
            print 'all ranges are nan...move fwd'
            mvFwd()
            bot_state = B_FWD
        return

    min_dist   = np.min(valid_r)
    left_dist  = valid_r[0]
    right_dist = valid_r[-1]
    ## Find laser that caused lowest valid range value. Disambiguate
    ## by giving preference to the leftmost laser
    min_las  = np.min(np.where(ranges==min_dist)[0])
    l_las    = np.min(np.where(ranges==left_dist)[0])
    r_las    = np.max(np.where(ranges==right_dist)[0])
    
    if min_las == 0:
        mvFwd()
        bot_state = B_FWD
    else:
        alignWithWall(min_las)

    #follow(min_las, ranges)


#    if min_dist < min_obj_dist:
#        print 'min dist < min_obj_dist', min_dist, ' | ',
#        if bot_state == B_FWD:
#            print 'move back'
#            mvBk()
#        elif bot_state == B_BK
#            print 'move fwd'
#            mvFwd()
#        else:
#            print 'not doing anything...bot_state:', bot_state
#
#
#    #if min_las >= CENTER-C_WIDTH and min_las <= CENTER-C_WIDTH:
 #   if bot_state == B_CLEAR:
 #       # safely away from walls, move fwd
 #       if min_dist > min_obj_dist:
 #           mvFwd()
 #       # close to wall (head on), turn right and align with wall
 #       else:
 #           angle = 90
 #           turnA(angle)
 #           wall_side = W_LEFT
 #           bot_state = B_WALL_FLW
 #   if bot_state == B_WALL_FLW:
 #       if min_dist > min_obj_dist:
 #           mvFwd()
 #       else:
 #           angle = getWallAngle(min_las)
 #           turnA(angle)
#
#    
#    #if min_dist > min_obj_dist:
#    #    mvFwd()
#    #else:
#    #    obj_dir = min_las * INC_ANGLE
#    #    if  obj_dir < 0:
#    #        turnL(np.abs(obj_dir + ANG_OFFSET))
#    #    else:
#    #        turnR(np.abs(obj_dir + ANG_OFFSET))
#    
#    #    print min_dist, min_las, obj_dir

def follow(min_las, ranges):
    global bot_state
    if ranges[CENTER] < min_obj_dist:
        print 'too close ahead...b_state:', bot_state, ' ',
        if bot_state == B_BK:
            print 'moving fwd'
            mvFwd()
            bot_state = B_FWD
        else:
            print 'moving back'
            mvBk()
            bot_state = B_BK
    elif ranges[min_las] < min_obj_dist:
        print 'too close min...b_state:', bot_state, ' ',
        if bot_state == B_BK:
            print 'moving fwd'
            mvFwd()
            bot_state = B_FWD
        else:
            print 'moving back'
            mvBk()
            bot_state = B_FWD
    else:
        alignWithWall(min_las)

def alignWithWall(laser_n):
    global bot_state
    angle = getWallAngle(laser_n)
    print angle
    turnA(angle)
    mvFwd()
    bot_state = B_FWD

def getSide(laser_n):
    if laser_n < CENTER:
        return LEFT
    elif laser_n == CENTER:
        return CENTER
    else:
        return RIGHT

def getWallAngle(laser_n):
    #diff_angle = (CENTER-laser_n) * INC_ANGLE
    global INC_ANGLE

    if INC_ANGLE == 0:
        INC_ANGLE = 60.0/640
    print 'an:', laser_n, INC_ANGLE
    diff_angle = laser_n * INC_ANGLE
    if diff_angle < 0:
        return 90 -(-ANG_OFFSET + diff_angle)
    return diff_angle

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
        spawnMBase()
        stop()
        #alignWithWall(int(sys.argv[1]))
        wallFollower(bot, x, y)
    except rp.ROSInterruptException:
        pass
