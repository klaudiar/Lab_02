from rock_paper_scissors import *


class Server:
    my_choice = 0

    def __init__(self, address, port):
        self.server(address, port)

    def server(self, address, port):
        connection = runSocket(address, port)

        answer = 0
        while answer == 0:
            while True:
                try:
                    self.choice = int(connection.recv(1024))    # data size - 1024
                    break
                except ValueError:
                    text = 'You must write a number'
                    print(text)
                    connection.send(text)
            text, answer = yourChoice(self.choice)
            connection.send(text)

        my_choice, text = serverChoice()
        connection.send(text)
        if self.choice-1 == my_choice or (self.choice == 1 and my_choice == 3):
            print("Client won")
            text = '!! WINNER !!'
        elif self.choice+1 == my_choice or (self.choice == 3 and my_choice == 1):
            print("Server won")
            text = 'LOOSER'
        elif self.choice == my_choice:
            print("Remis")
            text = 'Remis'
        connection.send(text)
        connection.close()

if __name__ == "__main__":
    host = 'localhost'
    port = 50001
    data_size = 1024
    server = Server(host, port)
