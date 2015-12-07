import socket

class Client_Tests:
    my_choice = 0
    def __init__(self):
        host = 'localhost'
        port = 50001
        self._server(host, port)


    def _server(self, address, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (address, port)
        print('bind to %s port %s' % server_address)
        self.sock.bind(server_address)
        self.sock.listen(1)
        i=0
        while i == 0:
            connection, client_address = self.sock.accept()
            self.choice = int(connection.recv(1024))    #data size - 1024

            if self.choice==500:
                sending_message = 'OK %s'% (self.choice)
                connection.send(sending_message.encode('utf-8'))
                print('OK %s' %(self.choice))
                i=5
            else: connection.send('WRONG'.encode('utf-8'))
            connection.send(''.encode('utf-8'))
            connection.send(''.encode('utf-8'))
        connection.close()




if __name__ == "__main__":
    server = Client_Tests()


