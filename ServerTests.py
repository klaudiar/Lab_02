import socket


class ServerTests:
    # firstly run Server in another terminal
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
        sock.sendto(message, server_address)
        response = sock.recv(1024)
        if response == 'You chose 1 - rock':
            print('OK')
        sock.recv(1024)
        sock.recv(1024)
        sock.close()

if __name__ == '__main__':
    client = ServerTests()