from controllers import ControllerBase

class ConsoleController(ControllerBase):
    def __init__(self):
        super().__init__()


    def update(self):
        print('Enter command (u/d/l/r/s/b):')
        cmd = input()

        self.left_stick_x = 0.0
        self.left_stick_y = 0.0
        self.right_stick_x = 0.0
        self.right_stick_y = 0.0
        self.back = False

        if cmd == 'l':
            self.right_stick_x = -1.0
        elif cmd == 'r':
            self.right_stick_x = 1.0
        elif cmd == 'u':
            self.left_stick_y = 1.0
        elif cmd == 'd':
            self.left_stick_y = -1.0
        elif cmd == 'b':
            self.back = True
    


