#!/usr/bin/env python

import sys
import rospy
from beginner_tutorials.srv import *
from geometry_msgs.msg import *

def add_two_ints_client(para):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(para)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    p = Point()
    p.x = x
    p.y = y
    para=list()
    para.append(p)
    para.append(p)
    param = [(1,2,3), (1,2,4)]
    print "Requesting %s+%s"%(x, y)
    print "%s + %s = %s"%(x, y, add_two_ints_client(param))

