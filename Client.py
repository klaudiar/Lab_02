__author__ = 'klaudiar'

import socket

class Client:
    def __init__(self,message):
        self.message = message
        self.client()

    def client(self):
        port = 50001
        host = 'localhost'
        server_address = (host, port)
        print('connecting to %s port %s' % server_address)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        if self.message == '': self.message = input('Answer: ')
        sock.sendto(self.message.encode('utf-8'),server_address)
        response = sock.recv(1024).decode('utf-8')
        print ('receive... \n\n%s' % response)
        while response == 'Wybrales zla liczbe':
            print('1')
            self.message = input('Answer: ')
            print('2')
            sock.sendto(self.message.encode('utf-8'),server_address)
            print('3')
            response = sock.recv(1024).decode('utf-8')
            print('4')
            print ('receive... \n\n%s' % response)
        response = sock.recv(1024).decode('utf-8')
        print (response)
        response = sock.recv(1024).decode('utf-8')
        print (response)
        sock.close()

if __name__ == '__main__':
    client = Client('')