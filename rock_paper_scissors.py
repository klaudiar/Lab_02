import socket
import random


def yourChoice(choice):
    if choice == 1:
        print('You chose rock')
        text = 'You chose %s - rock' % choice

    elif choice == 2:
        print('You chose paper')
        text = 'You chose %s - paper' % choice

    elif choice == 3:
        print('You chose scissors')
        text = 'You chose %s - scissors' % choice

    else:
        text = 'You chose wrong number'
        print(text)
        choice = 0
    return text, choice

def menu():
    print('Lets play in rock-paper-scissors\n')
    print('Choose one number: \n')
    print('1: rock\n2: paper\n3: scissors\n')

def runSocket(address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (address, port)
    menu()
    print('bind to %s port %s' % server_address)
    sock.bind(server_address)
    sock.listen(1)
    connection, client_address = sock.accept()
    return connection


def serverChoice():
    my_choice = random.randint(1, 3)
    text = 'Server chose %d - ' % my_choice

    if my_choice == 1:
        text = text + 'rock'
    elif my_choice == 2:
        text = text + 'paper'
    elif my_choice == 3:
        text = text + 'scissors'
    print(text, '\n')
    return my_choice, text
