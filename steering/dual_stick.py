from components.driving import DrivingComponentBase
from input import GamepadState


deadzone = 0.1


def steer(driver : DrivingComponentBase, state : GamepadState):
    if state.left_stick_y < -deadzone:
        driver.reverse(-state.left_stick_y)
    elif state.left_stick_y > deadzone:
        driver.forward(state.left_stick_y)
    elif state.right_stick_x < -deadzone:
        driver.turn_left(-state.right_stick_x)
    elif state.right_stick_x > deadzone:
        driver.turn_right(state.right_stick_x)
    else:
        driver.stop()
    