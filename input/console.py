from input import GamepadBase
from input import GamepadState

class ConsoleGamepad(GamepadBase):
    
    def get_current_state(self):

        print('Enter command (u/d/l/r/s/b):')
        cmd = input()

        state = GamepadState()
        state.left_stick_x = 0.0
        state.left_stick_y = 0.0
        state.right_stick_x = 0.0
        state.right_stick_y = 0.0
        state.back = False

        if cmd == 'l':
            state.right_stick_x = -1.0
        elif cmd == 'r':
            state.right_stick_x = 1.0
        elif cmd == 'u':
            state.left_stick_y = 1.0
        elif cmd == 'd':
            state.left_stick_y = -1.0
        elif cmd == 'b':
            state.back = True

        return state
            
    


