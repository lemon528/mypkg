#!/bin/bash
# SPDX-FileCopyrightText: 2025 kohei kobayashi
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source install/setup.bash


log_file="/tmp/sensor_simulator.log"
> $log_file

ros2 run mypkg sensor_simulator & NODE_PID=$!
ros2 topic echo /sensor_data std_msgs/msg/Float32 >> $log_file & TOPIC_PID=$!

sleep 30

res=0

if grep -q -E "data: [3-6]\.[0-9]+|data: 6\.9[0-9]*" $log_file; then
    echo "値が範囲内(3.0 - 7.0)に存在します"
else
    echo "範囲外を検出"
    res=1
fi

if grep -q -E "data: 3\.[0-9]*" $log_file; then
    echo "最小値(約3.0)を確認"
else
    echo "最小値を確認できません"
    res=1
fi

if grep -q -E "data: 6\.9[0-9]*" $log_file; then
    echo "最大値(約7.0)を確認"
else
    echo "最大値が確認できません"
    res=1
fi


if ps -p $NODE_PID > /dev/null 2>&1; then
    kill $NODE_PID
fi

if ps -p $TOPIC_PID > /dev/null 2>&1; then
    kill $TOPIC_PID
fi

if [ "$res" -eq 0 ]; then
    echo "全てのテストに成功しました。"
else
    echo "エラーが発生しました。"
fi

exit $res
