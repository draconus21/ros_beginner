#!/usr/bin/env python

import rospy as rp
from geometry_msgs.msg import Twist
from neeth_tbot.srv import Command
from Constants import *

cmd = Twist()

def get_cmd(new_cmd):
    global cmd
    cmd = new_cmd
    print 'new cmd:', cmd

def run_cmd():
    global cmd
    rp.init_node('botCmdMode', anonymous=True)
    pub = rp.Publisher(CMD_VEL, Twist, queue_size=Q_SIZE)
    srv = rp.Service('command', Command, get_cmd)

    r = rp.Rate(RATE)

    while not rp.is_shutdown():
        str = 'current_cmd: %s'%cmd
        #print str
        #rp.loginfo(str)
        pub.publish(cmd)
        r.sleep()

if __name__=='__main__':
    try:
       run_cmd()
    except rp.ROSInterruptException:
        pass
