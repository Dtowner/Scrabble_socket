import sys, getopt
import socket

ENCODING = 'ascii'

cmdArguments = sys.argv
argumentList = cmdArguments[1:]
unixOptions = 'ip:p'
gnuOptions = ['ip=', 'port=']

try:
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    print(str(err))
    sys.exit(2)

for currentArgument, currentValue in arguments:
    if currentArgument in ('-ip', '--ip'):
        ip = currentValue
    elif currentArgument in ('-p', '--port'):
        port = int(currentValue)

def cli_send_line(self, msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = self.send(msg[totalsent:].encode(ENCODING))
        if sent == 0:
            raise RuntimeError('socket connection broken')
        totalsent = totalsent + sent

def recieveResponse():
    global response
    response = so.recv(4026).decode(ENCODING)

    if 'OK Scrabble server at your service!USERJOIN' in response:
        print('OK Scrabble server at your service!')
        print(response.split('!', 1)[1].rsplit('!', 1)[0])
        return
    
    if response == ' ' or response == '1' or response == '1\n' or response == ' 1' or response == ' 1\n':
        return

    print(response)

    if 'NOK Tile not in hand!' in response:
        message = input()
        cli_send_line(so, message)

    if 'GOODBYE' in response:
        sys.exit()

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.connect((ip, port))

while True:
    recieveResponse()
    
    if response == '1' or response == '1\n' or response == ' 1' or response == ' 1\n':
        break

    while True:
        message = input()
        cli_send_line(so, message)

        recieveResponse()

        break

recieveResponse()

while True:
    while response != '':
        recieveResponse()

        if 'TURN' in response or 'WINNER' in response:
            message = input()
            cli_send_line(so, message)

        break

so.close()