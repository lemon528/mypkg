#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg resource_monitor_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'CPU usage:'
