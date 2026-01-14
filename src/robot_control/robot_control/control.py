import rclpy
from rclpy.node import Node
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
from geometry_msgs.msg import Twist
import math

class Control(Node):
    def __init__(self):
        super().__init__('control')

        self.client = RemoteAPIClient()
        self.sim = self.client.require('sim')

        self.base_joint = self.sim.getObject('/joint1')
        self.shoulder_joint = self.sim.getObject('/joint2')
        self.radar_joint = self.sim.getObject('/joint3')

        self.upper_limit = math.radians(90 - 41.1)
        self.lower_limit = math.radians(0 - 41.1)
        self.multiplier = math.radians(2)
        self.increment = math.radians(1)

        self.subscription=self.create_subscription(Twist , '/cmd_vel' , self.controller, 10)

        self.sim.startSimulation()
        self.get_logger().info('starting control bridge...')

    def controller(self, msg):
        current_pos = self.sim.getJointPosition(self.shoulder_joint)
        current_base_pos = self.sim.getJointPosition(self.base_joint)

        if(msg.linear.x>0):
            shoulder=1
        else:
            if(msg.linear.x<0):
                shoulder=-1
            else:
                shoulder=0

        if(msg.angular.z>0):
            base=1
        else:
            if(msg.angular.z<0):
                base=-1
            else:
                base=0
            
        elevation = current_pos + (shoulder * self.increment)
        azimuth = current_base_pos + (base * self.multiplier)
        radar_gaze = -elevation

        self.get_logger().info(f'{current_pos}')
        self.sim.setJointTargetPosition(self.base_joint , azimuth)
        self.sim.setJointTargetPosition(self.shoulder_joint , elevation)
        self.sim.setJointTargetPosition(self.radar_joint , radar_gaze)


def main(args=None):

    rclpy.init(args=args)
    control_node = Control()

    try:
        rclpy.spin(control_node)
    
    except KeyboardInterrupt:
        pass

    finally:
        control_node.sim.stopSimulation()
        control_node.destroy_node()
        rclpy.shutdown()

if __name__== '__main__':
    main()