from abc import ABC, abstractmethod

class ControllerBase():
    def __init__(self):

        # Initialize the stick values

        self.back = False
        self.left_stick_x = 0.0
        self.left_stick_y = 0.0
        self.right_stick_x = 0.0
        self.right_stick_y = 0.0
        super().__init__()

    @abstractmethod
    def update(self):
        pass


class InputState:
    def __init__(self):
        self.left_stick_x = 0.0
        self.left_stick_y = 0.0
        self.right_stick_x = 0.0
        self.right_stick_y = 0.0