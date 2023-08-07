from abc import ABC, abstractmethod

class GamepadBase():
      
    @abstractmethod
    def get_current_state(self):
        pass


class GamepadState:
    def __init__(self):
        self.left_stick_x = 0.0
        self.left_stick_y = 0.0
        self.right_stick_x = 0.0
        self.right_stick_y = 0.0