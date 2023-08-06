from abc import ABC, abstractmethod
from components import ComponentBase

class DrivingComponentBase(ComponentBase):
    def __init__(self, rover, left_motor, right_motor):
        super().__init__(rover)
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.left_motor.reset()
        self.right_motor.reset()
        self.left_throttle = 0
        self.right_throttle = 0
        
    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def thrust(self, left_thrust, right_thrust):
        pass

    @abstractmethod
    def forward(self, thrust):
        pass

    @abstractmethod
    def reverse(self, thrust):
        pass

    @abstractmethod
    def turn_left(self, thrust):
        pass

    @abstractmethod
    def turn_right(self, thrust):
        pass
