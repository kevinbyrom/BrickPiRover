from components.controllers import ControllerBase
from input import GamepadBase
from input import GamepadState
from components.driving.tracks import TracksComponent

from steering.dual_stick import steer


class ManualControllerComponent(ControllerBase):
    def __init__(self, rover, gamepad, tracks):
        super().__init__(rover)
        self.gamepad = gamepad
        self.tracks = tracks
        self.steering_behavior = steer
        

    def update(self):

        state = self.gamepad.get_current_state()
        
        if state is not None:
            steer(self.tracks, state)


            
    


