from rover import Rover
from controllers import ControllerBase

deadzone = 0.1


class DiscreteSteering():
    def apply(self, rover, controller):
        if controller.left_stick_y < -deadzone:
            rover.reverse(-controller.left_stick_y)
        elif controller.left_stick_y > deadzone:
            rover.forward(controller.left_stick_y)
        elif controller.right_stick_x < -deadzone:
            rover.turn_left(-controller.right_stick_x)
        elif controller.right_stick_x > deadzone:
            rover.turn_right(controller.right_stick_x)
        else:
            rover.stop()