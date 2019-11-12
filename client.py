import socket
import sys
import platform
import getpass

counter = 0
host = '127.0.0.1'
port = 12345
ENCODING = 'ascii'
global message
message = " "
global data



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    try:
        server.connect((host, port))
        print("Connected")
    except:
        print("Couldn't connect to server")


    while True:

        while counter == 0:
            message = " Hello, 1.0.1, python/" + str(platform.python_version()) + ", " + str(platform.system()) + ", " + str(getpass.getuser())
        #print(message)

            hello_data = server.recv(2048)
        #print("test hello: ", data.decode())
            if "Hello" in hello_data.decode():
                print(message)
                server.sendall(bytes(message, ENCODING))
            else:
                print("Goodbye")
                break

        ##print(message)
        #server.sendall(bytes(message, ENCODING))
            ok_data = server.recv(2048)
            print('Recieved: ', ok_data.decode())
            default_uname = str(getpass.getuser())
            server.sendall(bytes(default_uname, ENCODING))
            ok_name_data = server.recv(2048)
            print(str(ok_name_data.decode()))

            counter = 1

        while True:
            message = input('Type command to execute: ')
            if message == "quit":
                server.sendall(bytes(message, ENCODING))
                data = server.recv(2048)
                break

            elif "USERSET" in message:
                server.sendall(bytes(message, ENCODING))
                data = server.recv(2048)
                new_name = input('Enter new name to change to: ')
                server.sendall(bytes(new_name, ENCODING))

            elif message == "quit":
                server.sendall(bytes(message, ENCODING))
                data = server.recv(2048)
                break
            else:
                msg = "NOK: Unrecognized command"

        if "Goodbye" in data.decode():
            print("Goodbye")
            break
    server.close()
