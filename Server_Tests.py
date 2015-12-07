__author__ = 'klaudiar'

import socket
from Server import *

class Server_Tests:
    def __init__(self):
        self.test()

    def test(self):
        port = 50001
        host = 'localhost'
        server_address = (host, port)
        print('connecting to %s port %s' % server_address)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        message = '1'
        sock.sendto(message.encode('utf-8'),server_address)
        response = sock.recv(1024).decode('utf-8')
        print(type(response))
        if response == "Wybrales 1 - kamien":
            print('OK')
        sock.recv(1024).decode('utf-8')
        sock.recv(1024).decode('utf-8')
        sock.close()

if __name__ == '__main__':
    client = Server_Tests()