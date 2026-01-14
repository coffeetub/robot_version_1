from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        
        Node(
            package='robot_control',      
            executable='control',   
            name='control',
            output='screen'
        ),

        Node(
            package='teleop_twist_keyboard',
            executable='teleop_twist_keyboard',
            name='teleop_node',
            output='screen',
            prefix='xterm -e',           
            parameters=[{
                'speed': 0.5,
                'turn': 1.0
            }]
        )
    ])