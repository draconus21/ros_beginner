#!/usr/bin/env python

import sys
import rospy as rp
from geometry_msgs.msg import Twist
from turtlebot_a1.srv import *
from constants import *

def nullVel():
    vel = Twist()
    
    vel.linear.x = 0.0
    vel.linear.y = 0.0
    vel.linear.z = 0.0

    vel.angular.x = 0.0
    vel.angular.y = 0.0
    vel.angular.z = 0.0

    return vel

def simpleClient(vel):
    print 'waiting for serivce...'
    rp.wait_for_service(MOVE_BOT_SRV)
    print 'Got lock on service'

    try:
        mv_srv = rp.ServiceProxy(MOVE_BOT_SRV, MoveBot)
        status = mv_srv(vel)
        return status.status
    except rp.ServiceExeption as e:
        print 'Service call failed:', e


if __name__=='__main__':
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        z = int(sys.argv[2])
    else:
        x = 1.0
        z = 1.0

    vel = nullVel()
    vel.linear.x = x
    vel.angular.z = z

    print 'Requesting %s, %s'%(x, z)
    print 'Status:', simpleClient(vel)
