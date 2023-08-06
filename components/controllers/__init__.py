from abc import ABC, abstractmethod
from components import ComponentBase

class ControllerBase(ComponentBase):
    def __init__(self, rover):
        super().__init__(rover)
        
        # Initialize the stick values

        self.back = False
        self.left_stick_x = 0.0
        self.left_stick_y = 0.0
        self.right_stick_x = 0.0
        self.right_stick_y = 0.0
        

    @abstractmethod
    def update(self):
        pass


class InputState:
    def __init__(self):
        self.left_stick_x = 0.0
        self.left_stick_y = 0.0
        self.right_stick_x = 0.0
        self.right_stick_y = 0.0