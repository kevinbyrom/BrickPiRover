from rover import Rover

rover = Rover()

try:
    rover.startup()

    while True:
        rover.update()

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    rover.shutdown()