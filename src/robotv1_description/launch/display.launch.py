from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        # Publishes TF from URDF
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            arguments=['urdf/robot.urdf'],
            output='screen'
        ),

        # GUI sliders for joints
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen'
        ),

        # RViz
        Node(
            package='rviz2',
            executable='rviz2',
            output='screen'
        )

    ])
