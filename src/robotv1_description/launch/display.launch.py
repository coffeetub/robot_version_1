from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        # Publishes TF from URDF
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            arguments=['/home/krishna/robot_version_1/src/robotv1_description/urdf/robot_1.urdf'],
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
