import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    resource_monitor = launch_ros.actions.Node(
        package='mypkg',
        executable='resource_monitor',
        output='screen'
    )
    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen'
    )

    return launch.LaunchDescription([resource_monitor, listener])
