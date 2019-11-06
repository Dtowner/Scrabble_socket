import socket
import sys
import platform

port = 12345
ENCODE = 'UTF-8'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), port))
    while True:
        msg = s.recv(2048)
        print(msg.decode(ENCODE))
