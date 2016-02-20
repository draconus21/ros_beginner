#!/usr/bin/env python

import sys
import numpy as np
import rospy as rp
from geometry_msgs.msg import Twist, Pose
from gazebo_msgs.msg import ModelStates, ModelState
from gazebo_msgs.srv import SetModelState
from sensor_msgs.msg import LaserScan

works = False
def callback(m_state):
    global works

    obj_list = np.array(m_state.name)
    m_base = np.where(obj_list == 'mobile_base')[0][0]
    pose   = m_state.pose[m_base]
    ori    = pose.orientation
    print ori
    works = True

def spawnMBase(x,  y):
    mState = ModelState()
    mState.model_name = 'mobile_base'
    mState.pose.position.x = x
    mState.pose.position.y = y
    mState.pose.position.z = 0
    mState.pose.orientation.x = 0
    mState.pose.orientation.y = 0
    mState.pose.orientation.z = 0
    mState.pose.orientation.w = 1

    rp.wait_for_service('/gazebo/set_model_state')

    try:
        sms = rp.ServiceProxy('/gazebo/set_model_state', SetModelState)
        print 'Model State: ',  str(mState)
        sms(mState)
    except rp.ServiceException as e:
        print 'Service Exception:', e

def getMBasePosition():
    sub = rp.Subscriber('/gazebo/model_states', ModelStates, callback, queue_size=1000)
    pub = rp.Publisher('/gazebo/set_model_states', ModelStates, queue_size=1000)
    print 'test'
    rate = rp.Rate(4)
    while not rp.is_shutdown():
        rate.sleep()
    
if __name__=='__main__':
    rp.init_node('my_node')
#    x = 4
#    y = 4

#    if len(sys.argv) == 3:
#        x = int(sys.argv[1])
#        y = int(sys.argv[2])

    getMBasePosition()
#    spawnMBase(x, y)

