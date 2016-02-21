#!/usr/bin/env python

import sys
import time
import numpy as np
import rospy as rp
from geometry_msgs.msg import Twist, Pose, Point, Quaternion
from gazebo_msgs.msg import ModelState, ModelStates
from gazebo_msgs.srv import SetModelState
from turtlebot_a1.srv import MoveBot
from constants import *
 
vel  = Twist()

def spawnMBase(x=DEF_X, y = DEF_Y):
    mState = ModelState()
    mState.model_name = BOT
    pos = Point()
    pos.x = x
    pos.y = y
    pos.z = 0.0

    ori = Quaternion()
    ori.x = 0.0
    ori.y = 0.0
    ori.z = 0.0
    ori.w = 1.0

    mState.pose.position    = pos
    mState.pose.orientation = ori
    print serviceThis(SET_MODEL_STATE, SetModelState, mState)
    #print status, '-', msg


def mBaseStateCallback(mStates):
    #print np.array(mStates).shape

    obj_list = np.array(mStates.name)
    mBase    = np.where(obj_list == BOT)[0][0]
    print mStates.pose[mBase]
    #return mStates.post[mBase]

def subscribeThis(subName, subType, callback, q_size=Q_SIZE, loop=True, rate=RATE, dur=DURATION):
    nName = subName.split('/')[-1] + '_subscriber'
    rp.init_node(nName)
    sub = rp.Subscriber(subName, subType, callback, queue_size=q_size)
    r   = rp.Rate(rate)
    if loop == True:
        while not rp.is_shutdown():
            r.sleep()
    else:
        endTime = time.time() + dur
        while time.time() < endTime:
            r.sleep()

def getMBaseState(loop=True, dur=DURATION):
    print 'getting state'
    #rp.init_node('MBaseState')
    subscribeThis(MODEL_STATES, ModelStates, mBaseStateCallback, loop=loop, dur=dur)

def serviceThis(srvName, cmdType, srvCmd):
    nName = srvName.split('/')[-1] + '_service'
#    rp.init_node(nName)
    print 'init node:', nName
    print 'waiting for service:', srvName
    rp.wait_for_service(srvName)
    print 'got lock on serivce:', srvName

    try:
        sms = rp.ServiceProxy(srvName, cmdType)
        print 'service name:', srvName
        print 'serivce cmd val:', str(srvCmd)
        return sms(srvCmd)
    except rp.ServiceException as e:
        print 'Service Exception: ', srvName, '\n', e
        return -1

def twist_no_vel():
    vel = Twist()
    
    vel.linear.x = 0.0
    vel.linear.y = 0.0
    vel.linear.z = 0.0

    vel.angular.x = 0.0
    vel.angular.y = 0.0
    vel.angular.z = 0.0

    return vel

def pub_cmd(vel):
    return serviceThis(MOVE_BOT_SRV, MoveBot, vel)

def move(direction, dur, vel=FWD_SPD):
    cmd = twist_no_vel()
    if direction == FWD:
        cmd.linear.x = vel
    elif direction == BACK:
        cmd.linear.x = -vel
    pub_cmd(cmd)
    rp.sleep(dur)
    stop()

def mvFwd(dur=DURATION, vel=FWD_SPD):
    move(direction=FWD, dur=dur, vel=vel)

def mvBk(dur=DURATION, vel=FWD_SPD):
    move(direction=BACK, dur=dur, vel=vel)

def turn(direction, dur, vel = ANG_SPD):
    cmd = twist_no_vel()
    if direction == LEFT:
        cmd.angular.z = vel
    elif direction == RIGHT:
        cmd.angular.z = -vel
    pub_cmd(cmd)
    rp.sleep(dur)
    stop()

def turnL(dur=DURATION, vel=ANG_SPD):
    turn(direction=LEFT, dur=dur, vel=vel)

def turnR(dur=DURATION, vel=ANG_SPD):
    turn(direction=RIGHT, dur=dur, vel=vel)

def turnA(angle, vel=ANG_SPD):
    rad = angle * np.pi /180
    dur = np.abs(rad/vel)
    if dur == 0:
        print 'duration: 0'
        return 
    print 'turning for:', dur
    if angle == 0:
        print 'angle:', angle

    if angle > 0:
        print 'turning right at angle:', angle
        turnR(dur, vel)
    else:
        print 'turning left at angle:', angle
        turnL(dur, vel)
def stop():
    cmd = twist_no_vel() 
    pub_cmd(cmd)

if __name__=='__main__':
    #rp.init_node('botBasic')
    #spawnMBase(int(sys.argv[1]), int(sys.argv[2]))
    spawnMBase()
    ang = 0
    vel = ANG_SPD
    if len(sys.argv) > 1:
        ang = int(sys.argv[1])
    if len(sys.argv) > 2:
        vel = int(sys.argv[2])

    mvFwd(2)
    #turnA(ang, vel)
    #getMBaseState(False)
    #if len(sys.argv) == 3:
    #    if str(sys.argv[1]) == 'f':
    #        mvFwd(int(sys.argv[2]))
    #    elif str(sys.argv[1]) == 'b':
    #        mvBk(int(sys.argv[2]))
    #    elif str(sys.argv[1]) == 'l':
    #        turnL(int(sys.argv[2]))
    #    elif str(sys.argv[1]) == 'r':
    #        turnR(int(sys.argv[2]))
    #    else:
    #        print 'invalid command'
    #else:
    #    print 'Specify motion command'
    #print '*' * 30
    #getMBaseState(False)
