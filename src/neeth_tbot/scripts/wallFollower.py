#!/usr/bin/env python

import rospy as rp
from neeth_tbot.srv import Command
from geometry_msgs.msg import Twist, Pose
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState
from sensor_msgs.msg import LaserScan
from Constants import *
from command import *

N_LASER   = 640
C_WIDTH   = 2
MIN_RANGE = 100
MAX_RANGE = 0
MIN_ANGLE = 100
MAX_ANGLE = 0
INC_ANGLE = 1
MAX_SIZE  = N_LASER
CENTER    = N_LASER/2

init = True
vel  = Twist()

def get_cmd2(cmd):
    rp.init_node('constVel');
    pub = rp.Publisher(CMD_VEL, Twist, queue_size=Q_SIZE)
    r = rp.Rate(RATE)

    while not rp.is_shutdown():
        str = 'cmd: %s'%cmd
        print str
        pub.publish(cmd)
        r.sleep()

def twist_no_vel():
    vel = Twist()
    
    vel.linear.x = 0.0
    vel.linear.y = 0.0
    vel.linear.z = 0.0

    vel.angular.x = 0.0
    vel.angular.y = 0.0
    vel.angular.z = 0.0

    return vel

def move(direction, dur):
    cmd = twist_no_vel()
    if direction == FWD:
        cmd.linear.x = FWD_SPD
    elif direction == BACK:
        cmd.linear.x = -FWD_SPD
    get_cmd(cmd)
    rp.sleep(dur)
    stop()

def mvFwd(dur=DURATION):
    move(direction=FWD, dur=dur)

def mvBk(dur=DURATION):
    move(direction=BACK, dur=dur)

def turn(direction, dur):
    cmd = twist_no_vel()
    if direction == LEFT:
        cmd.angular.z = ANG_SPD
    elif direction == RIGHT:
        cmd.angular.z = -ANG_SPD
    get_cmd(cmd)
    rp.sleep(dur)
    stop()

def turnL(dur=DURATION):
    turn(direction=LEFT, dur=dur)

def turnR(dur=DURATION):
    turn(direction=RIGHT, dur=dur)
def stop():
    cmd = twist_no_vel() 
    get_cmd(cmd)

def init_me():
    rp.init_node('wallFollower')
    print 'waiting....'
    rp.wait_for_service('command')
    print 'service available'
    vel_srv = rp.ServiceProxy('command', Command)

if __name__=='__main__':
    init_me()
    print 'mvfwd'
    mvFwd(3)
    print 'mvBk'
    mvBk()
    print 'left'
    turnL(3)
    print 'right'
    turnR(3)
