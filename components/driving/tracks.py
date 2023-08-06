from components import ComponentBase
from components.driving import DrivingComponentBase

class TracksComponent(DrivingComponentBase):
    def update(self):

        # Convert the motor values to -100 / 100 and send output to the NXT motor
        # TODO: make this a little more configurable
        left_power = self.left_throttle * 100
        right_power = self.right_throttle * 100

        print('Setting motor powers: {}, {}'.format(left_power, right_power))
        self.left_motor.set_power(50)#left_power)
        self.right_motor.set_power(50)#right_power)
    

    def stop(self):
        print('Stopping')
        self.left_throttle = 0.0
        self.right_throttle = 0.0

    def thrust(self, left_thrust, right_thrust):
        print('Thrusting')
        self.left_throttle = left_thrust
        self.right_throttle = right_thrust

    def forward(self, thrust):
        print('Moving forward')
        self.left_throttle = thrust
        self.right_throttle = thrust

    def reverse(self, thrust):
        print('Moving back')
        self.left_throttle = -thrust
        self.right_throttle = -thrust

    def turn_left(self, thrust):
        print('Turning left')
        self.left_throttle = -thrust
        self.right_throttle = thrust

    def turn_right(self, thrust):
        print('Turning right')
        self.left_throttle = thrust
        self.right_throttle = -thrust
