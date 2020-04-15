from rover import Rover
from controllers import ControllerBase

deadzone = 0.05


class SingleStickSteering():
    def apply(self, rover, controller):
        if abs(controller.left_stick_x) > deadzone or abs(controller.left_stick_y) > deadzone:
            left_power = controller.left_stick_y - controller.left_stick_x
            right_power = controller.left_stick_y + controller.left_stick_x
            rover.thrust(left_power, right_power)
        else:
            rover.stop()