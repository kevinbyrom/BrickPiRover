from components import ComponentBase
from components.driving import DrivingComponentBase

class TracksComponent(DrivingComponentBase):
    def update(self):

        # Convert the motor values to -100 / 100 and send output to the NXT motor
        # TODO: make this a little more configurable
        left_power = self.left_thrust * 100
        right_power = self.right_thrust * 100

        print('Setting motor powers: {}, {}'.format(left_power, right_power))
        self.left_motor.set_power(left_power)
        self.right_motor.set_power(right_power)
    

    def stop(self):
        print('Stopping')
        self.left_thrust = 0.0
        self.right_thrust = 0.0

    def thrust(self, left_thrust, right_thrust):
        print('Thrusting')
        self.left_thrust = left_thrust
        self.right_thrust = right_thrust

    def forward(self, thrust):
        print('Moving forward')
        self.left_thrust = thrust
        self.right_thrust = thrust

    def reverse(self, thrust):
        print('Moving back')
        self.left_thrust = -thrust
        self.right_thrust = -thrust

    def turn_left(self, thrust):
        print('Turning left')
        self.left_thrust = -thrust
        self.right_thrust = thrust

    def turn_right(self, thrust):
        print('Turning right')
        self.left_thrust = thrust
        self.right_thrust = -thrust
