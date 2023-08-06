from components.driving import DrivingComponentBase
from components.controllers import InputState

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

def steer(driver : DrivingComponentBase, state : InputState):
    if abs(state.left_stick_x) > deadzone or abs(state.left_stick_y) > deadzone:
        
        thrust_pct = abs(state.left_stick_y)
        thrust_power = state.left_stick_y * thrust_pct

        left_turn_power = state.left_stick_x * (1 - thrust_pct)
        right_turn_power = -left_turn_power * (1 - thrust_pct)

        driver.thrust(thrust_power + left_turn_power, thrust_power + right_turn_power) 
    else:
        driver.stop()
    