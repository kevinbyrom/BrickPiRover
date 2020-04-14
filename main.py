from rover import Rover
from joypads.console import ConsoleJoypad
from joypads.udp import UdpJoypad

deadzone = 0.1

rover = Rover()
joypad = UdpJoypad()#ConsoleJoypad()

try:
    rover.startup()

    while joypad.back == False:

        # Move rover based on joypad

        joypad.update()

        if joypad.left_stick_y < -deadzone:
            rover.reverse(-joypad.left_stick_y)
        elif joypad.left_stick_y > deadzone:
            rover.forward(joypad.left_stick_y)
        elif joypad.right_stick_x < -deadzone:
            rover.turn_left(-joypad.right_stick_x)
        elif joypad.right_stick_x > deadzone:
            rover.turn_right(joypad.right_stick_x)
        else:
            rover.stop()

        # Update the rover to control the BP

        rover.update()

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    rover.shutdown()