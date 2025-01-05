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
ros2 topic echo /Noisy_sensor_data std_msgs/msg/Float32 >> $log_file & TOPIC_PID=$!

sleep 30

res=0

grep -q -E "data: [3-6]\.[0-9]+|data: 6\.9[0-9]*" $log_file && echo "値が範囲内(3.0 - 7.0)に存在します。" || { echo "範囲外を検出"; res=1; }

grep -q -E "data: 3\.[0-9]*" $log_file && echo "最小値(約3.0)を確認" || { echo "最小値が確認できません"; res=1; }

grep -q -E "data: 6\.9[0-9]*" $log_file && echo "最大値(約7.0)を確認" || { echo "最大値が確認できません"; res=1; }

kill $NODE_PID $TOPIC_PID
wait $NODE_PID $TOPIC_PID 2>/dev/null

if [ "$res" -eq 0 ]; then
    echo "全てのテストに成功しました。"
else
    echo "エラーが発生しました。"
fi

exit $res
