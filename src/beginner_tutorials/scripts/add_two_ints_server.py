#!/usr/bin/env python

from beginner_tutorials.srv import *

import rospy

def handle_add_two_ints(req):
    print "Returning ", req.a, " + ", req.b, " = ", (req.a+req.b)
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_serv2():
    rospy.init_node('add_two_ints_serv')
    s = rospy.Service('add_two_in22', AddTwoInts, handle_add_two_ints)
    print "!Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_serv2()

