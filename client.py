# Import socket module
import socket
import sys


def Main():
    Encode = 'ascii'
    # local host IP '127.0.0.1'
    host = '127.0.0.1'
    # Define the port on which you want to connect
    port = 12345
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # connect to server on local computer
    s.connect((host,port))
    # message you send to server
    hello = "Hello"
    s.send(hello.encode(Encode))
    while True:


        ans = input('\nWhat would you like to do? :')
        if (ans == 'userset'):
            continue
        elif(ans == 'quit'):
            break
        elif (ans == 'userchange'):
            continue
        elif(ans == 'userjoin'):
            continue
        elif(ans == 'ready'):
            continue
        elif(ans == 'place'):
            continue
        elif(ans == 'pass'):
            continue
        elif(ans == 'exchange'):
            continue
        else:
            continue

        # message sent to server
        s.send(ans.encode(Encode))

        # messaga received from server
        data = s.recv(1024)
        print(str(data.decode('ascii')))

    # close the connection
    s.close()



if __name__ == '__main__':
    Main()
