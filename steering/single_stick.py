from rover import Rover
from controllers import ControllerBase

deadzone = 0.05

'''
        0% <-> 100%
         (1,1)
           |
           |
 (-1,1) --- --- (1,-1)
           |
           |
        (-1,-1)
'''

class SingleStickSteering():
    def apply(self, rover, controller):
        if abs(controller.left_stick_x) > deadzone or abs(controller.left_stick_y) > deadzone:
            
            thrust_pct = abs(controller.left_stick_y)
            thrust_power = controller.left_stick_y * thrust_pct

            left_turn_power = controller.left_stick_x * (1 - thrust_pct)
            right_turn_power = -left_turn_power * (1 - thrust_pct)

            rover.thrust(thrust_power + left_turn_power, thrust_power + right_turn_power) 
        else:
            rover.stop()