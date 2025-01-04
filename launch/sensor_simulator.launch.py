# SPDX-FileCopyrightText: 2025 kohei kobayashi
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    sensor_simulator = launch_ros.actions.Node(
        package='mypkg',
        executable='sensor_simulator',
        output='screen'
        )

    return launch.LaunchDescription([sensor_simulator])
