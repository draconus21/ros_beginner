#!/usr/bin/env python

import rospy as rp
from geometry_msgs.msg import Twist
from turtlebot_a1.srv import *
from constants import *

cmd = Twist()

def nullVel():
    vel = Twist()

    vel.linear.x = 0.0
    vel.linear.y = 0.0
    vel.linear.z = 0.0

    vel.angular.x = 0.0
    vel.angular.y = 0.0
    vel.angular.z = 0.0

    return vel

def new_cmd(new_vel):
    global cmd
    cmd = new_vel.vel
    return 1

def exec_cmd():
    global cmd
    rp.init_node('cmd_bot')
    pub = rp.Publisher(CMD_VEL, Twist, queue_size=Q_SIZE)
    srv = rp.Service(MOVE_BOT_SRV, MoveBot, new_cmd)
    r = rp.Rate(DURATION)
    print 'Ready for new commands'
    
    while not rp.is_shutdown():
        str = 'current cmd: \n%s'%cmd
        print str
        pub.publish(cmd)
        r.sleep()

if __name__=='__main__':
    try:
        exec_cmd()
    except rp.ROSInterruptException:
        pass
    
