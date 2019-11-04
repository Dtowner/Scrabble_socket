# import socket programming library
import socket
import string
import sys
from _thread import *
import threading
import random
# thread fuction
def threaded(c):
    while True:

        # data received from client
        data = c.recv(1024)
        print(str(data))
        player_counter += 1
        if (data == 'quit'):
            print('Bye')
            break
        c.send(data)
    # connection closed
    c.close()

def Main():
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()
        print('Connected to :', addr[0], ':', addr[1])
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))

    s.close()
#tiles function
def tiles_generate(initial_hand_size):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(initial_hand_size))

def turn(user_number):
    switcher = {
    1: "player1",
    2: "player2",
    3: "player3",
    4: "player4",
    }

def board(letter, row, column ):
    print('hello')

if __name__ == '__main__':
    main()
