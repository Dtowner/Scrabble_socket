import socket
import sys
import platform



port = 12345


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), port))
    s.listen(5)

    clientsocket, address = s.accept()
    with clientsocket:
        print(f"Connected to: {address} ")

        clientsocket.send(bytes("Hello. Welcome to the server", 'UTF-8'))

        while True:
            data = clientsocket.recv(2048)
            if not data:
                break
            connection.sendall(data)
