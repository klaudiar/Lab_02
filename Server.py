import random
import socket

class Server:
    my_choice = 0
    def __init__(self, address, port):
        self._server(address, port)


    def _server(self, address, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (address, port)
        print('Zagrajmy w kamien, papier nozyce\n')
        print('Wybierz jeden numer: \n')
        print('1: kamien\n2: papier\n3: nozyce\n')
        print('bind to %s port %s' % server_address)
        self.sock.bind(server_address)
        i=0
        self.sock.listen(1)
        connection, client_address = self.sock.accept()
        while i == 0:
            self.choice = connection.recv(1024).decode('utf-8')    #data size - 1024
            if self.choice == '1':
                print('Wybrano kamien')
                text = 'Wybrales %s - kamien'% (self.choice)
                connection.send(text.encode('utf-8'))
                i=5
            elif self.choice == '2':
                print('Wybrano papier')
                text = 'Wybrales %s - papier'% (self.choice)
                connection.send(text.encode('utf-8'))
                i=5
            elif self.choice == '3':
                print('Wybrano nozyce')
                text = 'Wybrales %s - nozyce'% (self.choice)
                connection.send(text.encode('utf-8'))
                i=5
            else:
                print('Wybrales zla liczbe %s'% i)
                connection.send('Wybrales zla liczbe'.encode('utf-8'))

        my_choice = random.randint(1,3)

        if my_choice ==1:
            print('Serwer wybral kamien')
            text = 'Serwer wybral kamien'
            connection.send(text.encode('utf-8'))
        elif my_choice == 2:
            print('Serwer wybral papier')
            text = 'Serwer wybral papier'
            connection.send(text.encode('utf-8'))
        elif my_choice == 3:
            print('Serwer wybral nozyce')
            text = 'Serwer wybral nozyce'
            connection.send(text.encode('utf-8'))

        self.choice = int(self.choice)
        if self.choice-1 == my_choice or (self.choice==3 and my_choice==1):
            print("Klient wygral")
            connection.send('Wygrales'.encode('utf-8'))
        elif self.choice+1 == my_choice or (self.choice==1 and my_choice==3):
            print("Serwer wygral")
            connection.send('Przegrales'.encode('utf-8'))
        elif self.choice == my_choice:
            print("Remis")
            connection.send('Remis'.encode('utf-8'))


        connection.close()




if __name__ == "__main__":
    host = 'localhost'
    port = 50001
    data_size = 1024
    server = Server(host, port)


