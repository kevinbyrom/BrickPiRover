class Motor():
    def __init__(self, bp,  port):
        self.bp = bp
        self.port = port

    def reset(self):
        self.bp.offset_motor_encoder(self.port, self.bp.get_motor_encoder(self.port))

    def set_power(self, power):
        self.bp.set_motor_power(self.port, power)