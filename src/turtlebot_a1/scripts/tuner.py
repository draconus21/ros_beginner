#!/usr/bin/env python

import sys
import time
import numpy as np
import time
import rospy as rp
from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ModelStates
from sensor_msgs.msg import LaserScan
from wallFollower import spawnMe

nan = np.nan
stop = False
init = True
init_state = True

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

def cb2(mStates):
    global init_state

    objName = np.array(mStates.name)
    obj     = np.where(objName == 'mobile_base')[0][0]
    pose    = mStates.pose[obj]
    w       = pose.orientation.w
    angle   = np.arccos(w) * 180/np.pi
    print 'angle:', angle
    if init_state != True:
        if angle > 1e-3:
            rotate()
    init_state = False

i = 0
def rotate():
    global i
    print 'Rotating:', i
    i = i + 1
    pub = rp.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1000)
    rate = rp.Rate(2)
    vel  = Twist()

    vel.linear.x = 0
    vel.linear.y = 0
    vel.linear.z = 0

    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = 1

    pub.publish(vel)
    rate.sleep()


def dynamicTuner():
    rp.init_node('dynamic_tuner')

    spawnMe('mobile_base', 0, 0)

    sub = rp.Subscriber('/gazebo/model_states', ModelStates, cb2, queue_size=1000)
    rate = rp.Rate(1.0/4)
    while True:
        print 'Running'
        rate.sleep()

def tuner(lx=0, ly=0, lz=0, ax=0, ay=0, az=0, r=1):
    rp.init_node('tuner')

    spawnMe('mobile_base', 0, 0)
    pub = rp.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=1000)
    #sub = rp.Subscriber('/scan', LaserScan, callback, queue_size=1000)

    rate = rp.Rate(r)
    vel  = Twist()
    t = time.time()

    i = 0
    while not rp.is_shutdown():
        i = i + 1
        print i
        #if stop:
        #    break
#        spawnMe('mobile_base', 0, 0)
        vel.linear.x = lx
        vel.linear.y = ly
        vel.linear.z = lz

        vel.angular.x = ax
        vel.angular.y = ay
        vel.angular.z = az

        print 'start:', t, stop
        pub.publish(vel)
        rate.sleep()
#        if stop:
#            break
        stop_t = time.time()
        print 'stop_t:', stop_t
        print 'exec time:', (stop_t-t)
#        rp.signal_shutdown('got it')

if __name__=='__main__':
    lx = 0
    ly = 0
    lz = 0
    ax = 0
    ay = 0
    az = 0
    r  = 1.0
    if len(sys.argv) > 1:
        lx = int(sys.argv[1])
    if len(sys.argv) > 2:
        az = int(sys.argv[2])
    if len(sys.argv) > 3:
        r = float(sys.argv[3])
    if len(sys.argv) > 4:
        ly = int(sys.argv[4])
    if len(sys.argv) > 5:
        lz = int(sys.argv[5])
    if len(sys.argv) > 6:
        ay = int(sys.argv[6])
    if len(sys.argv) > 7:
        az = int(sys.argv[7])

#    tuner(lx, ly, lz, ax, ay, az, r)
    dynamicTuner()
