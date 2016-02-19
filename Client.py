import socket


class Client:
    def __init__(self, message):
        self.message = message
        self.client()

    def client(self):
        port = 50001
        host = 'localhost'
        server_address = (host, port)
        print('connecting to %s port %s' % server_address)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        if self.message == '':
            while True:
                try:
                    self.message = str(input('Answer: '))
                    break
                except NameError:
                    print('You must choose number')
                except SyntaxError:
                    print('You must choose number')

        sock.sendto(self.message, server_address)
        response = sock.recv(1024)
        print('receive... \n\n%s' % response)
        while response == 'You chose wrong number' or response == "You must write a number":
            while True:
                try:
                    self.message = str(input('Answer: '))
                    break
                except NameError:
                    print('You must choose number')
                except SyntaxError:
                    print('You must choose number')
            sock.sendto(self.message, server_address)
            response = sock.recv(1024)
            print('receive... \n\n%s' % response)
        response = sock.recv(1024)
        print(response, '\n')
        response = sock.recv(1024)
        print(response)
        sock.close()

if __name__ == '__main__':
    client = Client('')
