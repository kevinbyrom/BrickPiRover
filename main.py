import brickpi3
from rover import Rover

bp = brickpi3.BrickPi3()
rover = Rover(bp)

try:
    rover.startup()

    while True:
        rover.update()

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    rover.shutdown()