import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

class Rover:

    def __init__(self):
        print('Initializing rover...')
        self.left_motor = 0.0
        self.right_motor = 0.0

    def startup(self):
        BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A)) # reset encoder A
        BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D)) # reset encoder D

    def shutdown(self):
        BP.reset_all() 

    def update(self):
        print('Updating rover')

        # Convert the motor values to -100 / 100 and send output to the NXT motor

        left_power = self.left_motor * 100
        right_power = self.right_motor * 100
        print('Setting motor powers: {}, {}'.format(left_power, right_power))
        BP.set_motor_power(BP.PORT_A, left_power)
        BP.set_motor_power(BP.PORT_D, right_power)

    def stop(self):
        print('Stopping')
        self.left_motor = 0.0
        self.right_motor = 0.0

    def forward(self, power):
        print('Moving forward')
        self.left_motor = power
        self.right_motor = power

    def reverse(self, power):
        print('Moving back')
        self.left_motor = -power
        self.right_motor = -power

    def turn_left(self, power):
        print('Turning left')
        self.left_motor = -power
        self.right_motor = power

    def turn_right(self, power):
        print('Turning right')
        self.left_motor = power
        self.right_motor = -power