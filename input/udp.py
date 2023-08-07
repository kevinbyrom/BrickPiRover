from input import GamepadBase
from input import GamepadState
import socket
import json

bufferSize = 1024

class UdpGamepad(GamepadBase):
    def __init__(self, ip, port):
        super().__init__()
        self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.UDPServerSocket.bind((ip, port))

    def get_current_state(self):

        try:
            bytesAddressPair = self.UDPServerSocket.recvfrom(bufferSize)
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]

            message = message.decode("utf-8")
            data = message.split(",")

            state = GamepadState()
            state.left_stick_x = float(data[0])
            state.left_stick_y = float(data[1])
            state.right_stick_x = float(data[2])
            state.right_stick_y = float(data[3])
            
            return state

        except Exception as e:
            print('Error occured reading udp:' + e)
            return None
            
    


