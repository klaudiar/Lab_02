import unittest
import socket


class TestClientConnecting(unittest.TestCase):
    # This test is connected with TestRunClientConnecting, firstly run TestClientConnecting
    # and then TestRunClientConnecting in another terminal

    def testClientConnecting(self):
        address = 'localhost'
        port = 50001
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (address, port)
        print('bind to %s port %s' % server_address)
        self.sock.bind(server_address)
        self.sock.listen(1)

        connection, client_address = self.sock.accept()
        self.choice = int(connection.recv(1024))    # data size - 1024

        assert self.choice == 500, "Problem with connection"
        connection.send('OK')
        connection.send('')
        connection.send('')
        connection.close()

if __name__ == "__main__":
    unittest.main()
