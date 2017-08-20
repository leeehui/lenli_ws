# lenli_ws
lenli workspace of ros

# for multi-robot
##/etc/hosts
### usr1
<usr1 ip> usr1
<usr2 ip> usr2
### usr2
<usr1 ip> usr1
<usr2 ip> usr2

## ROS Defines
### usr1(as master)
ROS_MASTER=usr1
ROS_URI=http://usr1:11311
ROS_IP=<usr1 ip>
### usr2 
ROS_MASTER=usr1
ROS_URI=http://usr2:11311
ROS_IP=<usr2 ip>

# for Service
When embedding other Message descriptions, the type name may be relative (e.g. "Point32") if it is in the same package; otherwise it must be the full Message type (e.g. "std_msgs/String"). The only exception to this rule is Header.
NOTE: you must not use the names of built-in types or Header when constructing your own message types. 

e.g.
geometry_msgs/Point[] param

