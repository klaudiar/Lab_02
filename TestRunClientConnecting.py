from Client import *


class TestRunClientConnecting:
    # This test is connected with TestClientConnecting, firstly run TestClientConnecting
    # and then TestRunClientConnecting in another terminal
    def __init__(self):
        message = '500'
        Client(message)

if __name__ == "__main__":
    TestRunClientConnecting()

