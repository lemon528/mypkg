#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
log_file="/tmp/resource_monitor.log"
timeout 10 ros2 run mypkg resource_monitor > $log_file

cat $log_file |
grep 'CPU usage:'
