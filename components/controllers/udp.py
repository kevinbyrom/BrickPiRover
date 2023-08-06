from components.controllers import ControllerBase
from components.controllers import InputState
from components.driving.tracks import TracksComponent

from steering.dual_stick import steer
import socket
import json

bufferSize = 1024

class UdpControllerComponent(ControllerBase):
    def __init__(self, rover, ip, port, tracks):
        super().__init__(rover)
        self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.UDPServerSocket.bind((ip, port))
        self.steering_behavior = steer
        self.tracks = tracks

    def update(self):

        try:
            bytesAddressPair = self.UDPServerSocket.recvfrom(bufferSize)
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]

            message = message.decode("utf-8")
            data = message.split(",")

            state = InputState()
            state.left_stick_x = float(data[0])
            state.left_stick_y = float(data[1])
            state.right_stick_x = float(data[2])
            state.right_stick_y = float(data[3])
            
            steer(self.tracks, state)

        except Exception as e:
            print('Error occured reading udp:' + e)

            
    


