#!/usr/bin/env python

import sys
import numpy as np
import rospy as rp
from bot_basic import *
from constants import *

des = np.zeros(3)

def getDirVec(src, dest):
    dirVec = np.array(dest)-np.array(src)    
    return dirVec

def getDesAngle(dirVec):
    dirVec = np.array(dirVec)
    angle  = np.arctan(float(dirVec[1])/dirVec[0])
    angle  = np.abs(angle) * 180/np.pi
    if dirVec[0] < 0:
        angle = angle + 90
    if dirVec[1] < 0:
        angle = -angle
    return angle

def goalAngle(dirVec):
    angle  = getDesAngle(dirVec)
    w = mbState.pose.orientation.w
    z = mbState.pose.orientation.z
    c_angle = np.arccos(w) * 2 * 180/np.pi
    s_angle = np.arcsin(z) * 2 * 180/np.pi
    
    b_angle = np.abs(c_angle)
    if w < 0:
        b_angle = b_angle+90
    if z < 0:
        b_angle = -b_angle

    #print angle, b_angle, (b_angle+angle)
    return (b_angle+angle)

def bug2(src, des):
    [src_x, src_y] = src
    [des_x, des_y] = des
    
    spawnMBase(src_x, src_y)
    getMBaseState(loop=False)

    cur_x = mbState.pose.position.x
    cur_y = mbState.pose.position.y
    cur   = [cur_x, cur_y]

    while not reachedDestination(cur, des):
       dirVec = getDirVec(cur, des)
       angle  = goalAngle(dirVec)
       if np.abs(angle) > ANG_THRESH:
#           print 'turning at:', angle
           turnA(angle)
       else:
#           print 'dir:', dirVec
           mvFwd(vel=min(FWD_SPD, np.linalg.norm(dirVec)))
       #mvSpl(dirVec, DURATION)
       getMBaseState(loop=False)
       cur_x = mbState.pose.position.x
       cur_y = mbState.pose.position.y
       cur   = [cur_x, cur_y]
#       print cur 
    print 'reached:', des

def reachedDestination(x, y):
    x = np.array(x)
    y = np.array(y)
    dist = np.linalg.norm([x-y])
#    print 'dist:', dist
    if dist < DIST_THRESH:
        return True
    return False

if __name__ == '__main__':
    global des

    src_x = 0
    src_y = 0
    des_x = 0
    des_y = 0
    if len(sys.argv) > 2:
        des_x = int(sys.argv[1])
        des_y = int(sys.argv[2])
    if len(sys.argv) > 4:
        src_x = int(sys.argv[3])
        src_y = int(sys.argv[4])
    
    des = [des_x, des_y]
    src = [src_x, src_y]
    #getDesAngle(getDirVec(src, des))
    #spawnMBase(src_x, src_y)
    #stop()
    #getMBaseState(loop=False)
    #turnA(goalAngle(getDirVec(src, des)))
    #getMBaseState(loop=False)
   # goalAngle()
    #mvFwd()
    #getMBaseState(loop=False)
    #print mbState
    bug2(src, des)
