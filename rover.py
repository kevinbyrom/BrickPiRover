import brickpi3 # import the BrickPi3 drivers
from motor import Motor
from components.driving.tracks import TracksComponent
from components.controllers.udp import UdpControllerComponent

class Rover:

    def __init__(self):
        print('Initializing rover...')
        
        self.bp = brickpi3.BrickPi3()
        self.motor_a = Motor(self.bp, self.bp.PORT_A)
        self.motor_d = Motor(self.bp, self.bp.PORT_D)

        self.components = {}

        # Setup tracks

        tracks = TracksComponent(self, self.motor_a, self.motor.d)
        self.add_component(tracks)

        # Setup UDP controller

        udpController = UdpControllerComponent(self, "192.168.86.97", 20001)
        self.add_component(udpController)


    def startup(self):
        for c in self.get_all_components():
            c.startup()


    def shutdown(self):
        for c in self.get_all_components():
            c.shutdown()
        self.bp.reset_all() 


    def add_component(self, component):
        component_type = type(component).__name__
        self.components[component_type] = component


    def get_component(self, component_type):
        return self.components.get(component_type)


    def get_all_components(self):
        return self.components.itervalues()


    def update(self):
        print('Updating rover')
        for c in self.get_all_components():
            c.update()


