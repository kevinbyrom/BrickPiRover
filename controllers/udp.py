from controllers.base import ControllerBase
import socket
import json

localIP         = "192.168.86.97"
localPort       = 20001
bufferSize      = 1024

class UdpJoypad(ControllerBase):
    def __init__(self):
        super().__init__()
        self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.UDPServerSocket.bind((localIP, localPort))

    def update(self):

        try:
            bytesAddressPair = self.UDPServerSocket.recvfrom(bufferSize)
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]

            message = message.decode("utf-8")
            data = message.split(",")

            self.left_stick_x = float(data[0])
            self.left_stick_y = float(data[1])
            self.right_stick_x = float(data[2])
            self.right_stick_y = float(data[3])
            
        except Exception as e:
            print('Error occured reading udp:')
            print(e)
            self.left_stick_x = 0.0
            self.left_stick_y = 0.0
            self.right_stick_x = 0.0
            self.right_stick_y = 0.0
            self.back = False
    


