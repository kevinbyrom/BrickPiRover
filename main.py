from rover import Rover


rover = Rover()

#from controllers.console import ConsoleController
#ctl = ConsoleController()

from controllers.udp import UdpController
ctl = UdpController()

from steering.single_stick import SingleStickSteering
steering = SingleStickSteering()

try:
    rover.startup()

    while ctl.back == False:

        # Update the controller and apply steering

        ctl.update()

        steering.apply(rover, ctl)

        # Update the rover 

        rover.update()

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    rover.shutdown()