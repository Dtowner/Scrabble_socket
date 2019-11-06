import sys, getopt
import random
import socket

ENCODING = 'ascii'
    
cmdArguments = sys.argv
argumentList = cmdArguments[1:]
unixOptions = 'p:'
gnuOptions = 'port='

try:
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    print(str(err))
    sys.exit(2)

for currentArgument, currentValue in arguments:
    if currentArgument in ('-p', '--port'):
        port = int(currentValue)

try:
    port
except NameError:
    port = 9000

class Player:
    def __init__(self , addr):
        self.name = addr
        self.score = 0

class Board:
    def __init__(self):
        self.board = [[' 0 ' for i in range(15)] for j in range(15)]

        TWS = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
        DWS = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
        TLS = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        DLS = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

        for coordinate in TWS:
            self.board[coordinate[0]][coordinate[1]] = ' 4 '
        for coordinate in TLS:
            self.board[coordinate[0]][coordinate[1]] = ' 2 '
        for coordinate in DWS:
            self.board[coordinate[0]][coordinate[1]] = ' 3 '
        for coordinate in DLS:
            self.board[coordinate[0]][coordinate[1]] = ' 1 '

    def getBoard(self):
        board_str = '   |  ' + '  |  '.join(str(item) for item in range(10)) + '  | ' + '  | '.join(str(item) for item in range(10, 15)) + ' |'
        board_str += '\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n'
        board = list(self.board)
        for i in range(len(board)):
            if i < 10:
                board[i] = str(i) + '  | ' + ' | '.join(str(item) for item in board[i]) + ' |'
            if i >= 10:
                board[i] = str(i) + ' | ' + ' | '.join(str(item) for item in board[i]) + ' |'
        board_str += '\n   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n'.join(board)
        board_str += '\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'
        return board_str

    def boardArray(self):
        return self.board

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.bind(('', port))
so.listen(5)
print(f'Listening for a connection on port {port}...')

global data
startTick = 0

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
distribution = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]
bag = [[letters, points], distribution]
remainingLetters = 100
bagTick = 0

letterPoints = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

dictionary = open('/usr/share/dict/words')
dictList = dictionary.read()

for i in range(0, 2):
    x = random.randint(0, len(letters) - 1)
    for j in bag[0][0]:
        if (x == bag[0][0].index(j)):
            bag[1][x] += 1

def drawTiles(amount):
    count = 0
    tiles = ''

    while count < amount:
        x = random.randint(0, len(letters) - 1)

        for i in bag[0][0]:
            if x == bag[0][0].index(i):
                tiles = tiles + i + ' '
                bag[1][x] -= 1

                if bag[1][x] == 0:
                    for j in bag[0][1]:
                        if x == bag[0][1].index(j):
                            bag[0][0].remove(i)
                            bag[0][1].remove(j)
                            bag[1].remove(bag[1][x])

                break
        count += 1

    return tiles

players = []

while True:
    cli, raddr = so.accept()

    if sys.platform == 'darwin':
        cli.sendall((f'HELLO 1.0.1,Mac OS,Python/3.7.2,Cooper Fraser').encode(ENCODING))
    elif sys.platform == 'win32':
        cli.sendall((f'HELLO 1.0.1,Windows,Python/3.7.2,Cooper Fraser').encode(ENCODING))
    elif sys.platform == 'linux':
        cli.sendall((f'HELLO 1.0.1,Linux,Python/3.7.2,Cooper Fraser').encode(ENCODING))

    rhost, rport = raddr
    print(f'Received connection from {rhost} port {rport}')
    players.append(Player(rhost))

    data = cli.recv(4096).decode(ENCODING)

    while startTick != 1:
        if 'HELLO' not in data or 'QUIT' in data:
            print(data)
            cli.sendall((f'GOODBYE'.encode(ENCODING)))
            cli.close()
        elif (('HELLO 1.0.1,Mac OS,Python/3.7.2,Cooper Fraser') in data and ('HELLO 1.0.1,Windows,Python/3.7.2,Cooper Fraser') not in data and ('HELLO 1.0.1,Linux,Python/3.7.2,Cooper Fraser') not in data):
            print(data)
            cli.sendall((f'OK Scrabble server at your service!'.encode(ENCODING)))
            for i in range(len(players)):
                cli.sendall((f'USERJOIN ' + players[i].name).encode(ENCODING))
            startTick = 1
            break
        elif (('HELLO 1.0.1,Windows,Python/3.7.2,Cooper Fraser') in data and ('HELLO 1.0.1,Mac OS,Python/3.7.2,Cooper Fraser') not in data and ('HELLO 1.0.1,Linux,Python/3.7.2,Cooper Fraser') not in data):
            print(data)
            cli.sendall((f'OK Scrabble server at your service!'.encode(ENCODING)))
            for i in range(len(players)):
                cli.sendall((f'USERJOIN ' + players[i].name).encode(ENCODING))
            startTick = 1
            break
        elif (('HELLO 1.0.1,Linux,Python/3.7.2,Cooper Fraser') in data and ('HELLO 1.0.1,Windows,Python/3.7.2,Cooper Fraser') not in data and ('HELLO 1.0.1,Mac OS,Python/3.7.2,Cooper Fraser') not in data):
            print(data)
            cli.sendall((f'OK Scrabble server at your service!'.encode(ENCODING)))
            for i in range(len(players)):
                cli.sendall((f'USERJOIN ' + players[i].name).encode(ENCODING))
            startTick = 1
            break
        elif (('HELLO 1.0.1,Mac OS,Python/3.7.2,Cooper Fraser') not in data and ('HELLO 1.0.1,Windows,Python/3.7.2,Cooper Fraser') not in data and ('HELLO 1.0.1,Linux,Python/3.7.2,Cooper Fraser') not in data):
            print(data)
            cli.sendall((f'NOK Unsupported version!'.encode(ENCODING)))

        data = cli.recv(4096).decode(ENCODING)

    while True:
        data = cli.recv(4096).decode(ENCODING)
        cli.sendall(f' '.encode(ENCODING))
        
        if 'USERSET' in data and 'READY' not in data and 'QUIT' not in data:
            print(data)
            newName = data.split(' ', 1)[1].rsplit(' ', 1)[0]

            for i in players:
                if i.name == cli.getpeername()[0]:
                    cli.sendall((f'USERCHANGE ' + i.name + ' ' + newName).encode(ENCODING))
                    i.name = newName
        elif 'READY' in data and 'USERSET' not in data and 'QUIT' not in data:
            print(data)
            cli.sendall(f'1'.encode(ENCODING))
            break
        elif 'QUIT' in data and 'USERSET' not in data and 'READY' not in data:
            print(data)
            cli.sendall(f'GOODBYE'.encode(ENCODING))
        elif 'USERSET' not in data and 'READY' not in data and 'QUIT' not in data:
            print(data)
            cli.sendall(f'NOK Unrecognized command!'.encode(ENCODING))

    cli.sendall(f'STARTING'.encode(ENCODING))
    cli.sendall(f''.encode(ENCODING))

    score = 0

    tileset = drawTiles(7)
    board = Board()
    currentPlayer = players[0]

    passTick = False
    endTick = False

    while True:
        cli.sendall((f'SCORE ' + str(score) + ' ' + players[0].name).encode(ENCODING))
        cli.sendall((f'TILES ' + tileset).encode(ENCODING))
        cli.sendall((f'BOARDPUSH\n' + board.getBoard() + '\n').encode(ENCODING))
        cli.sendall((f'TURN ' + currentPlayer.name).encode(ENCODING))

        turnScore = 0
        currentScore = 0
        doubleWord = False
        tripleWord = False

        if players.index(currentPlayer) != len(players) - 1:
            currentPlayer = players[players.index(currentPlayer) + 1]
        else:
            currentPlayer = players[0]

        while True:
            data = cli.recv(4096).decode(ENCODING)
            print(data)

            if 'PASS' in data and passTick == False:
                print('debug')
                passTick = True
                break
            elif 'PASS' in data and passTick == True:
                endTick = True
                break

            if 'PLACE' in data and 'EXCHANGE' not in data:
                tilePlaced = (data.split('(', 1)[1].rsplit(',')[0]).upper()
                locationX = data.split(', ', 1)[1].rsplit(',')[0]
                locationY = data.split(', ', 1)[1].rsplit(', ')[1].rsplit(')')[0]

                boardArray = board.boardArray()
                
                if tilePlaced not in tileset:
                    while True:
                        cli.sendall(f'NOK Tile not in hand!'.encode(ENCODING))

                        data = cli.recv(4096).decode(ENCODING)
                        print(data)

                        tilePlaced = (data.split('(', 1)[1].rsplit(',')[0]).upper()
                        locationX = data.split(', ', 1)[1].rsplit(',')[0]
                        locationY = data.split(', ', 1)[1].rsplit(', ')[1].rsplit(')')[0]

                        if tilePlaced in tileset:
                            points = letterPoints[tilePlaced]
                    
                            if boardArray[int(locationX)][int(locationY)] == ' 0 ':
                                turnScore += points
                                currentScore += points
                            elif boardArray[int(locationX)][int(locationY)] == ' 1 ':
                                turnScore += points * 2
                                currentScore += points * 2
                            elif boardArray[int(locationX)][int(locationY)] == ' 2 ':
                                turnScore += points * 3
                                currentScore += points * 3
                            elif boardArray[int(locationX)][int(locationY)] == ' 3 ':
                                doubleWord = True
                            elif boardArray[int(locationX)][int(locationY)] == ' 4 ':
                                tripleWord = True

                            if doubleWord == True:
                                currentScore *= 2
                                turnScore += currentScore
                                currentScore = 0
                            elif tripleWord == True:
                                currentScore *= 3
                                turnScore += currentScore
                                currentScore = 0

                            score += turnScore
                            turnScore = 0

                            currentPlayer.score = score

                            boardArray[int(locationX)][int(locationY)] = ' ' + tilePlaced + ' '

                            for i in tileset:
                                if i == tilePlaced:
                                    tileset = list(tileset)
                                    tileset.remove(i)
                            
                                newTileset = ''
                                for j in tileset:
                                    if j == ' ':
                                        continue

                                    newTileset += j + ' '

                                tileset = newTileset

                                break

                            cli.sendall((f'TILES ' + tileset).encode(ENCODING))
                            cli.sendall((f'BOARDPUSH\n' + board.getBoard() + '\n').encode(ENCODING))
                            cli.sendall((f'TURN ' + currentPlayer.name).encode(ENCODING))
                            break
                else:
                    points = letterPoints[tilePlaced]
                    
                    if boardArray[int(locationX)][int(locationY)] == ' 0 ':
                        turnScore += points
                        currentScore += points
                    elif boardArray[int(locationX)][int(locationY)] == ' 1 ':
                        turnScore += points * 2
                        currentScore += points * 2
                    elif boardArray[int(locationX)][int(locationY)] == ' 2 ':
                        turnScore += points * 3
                        currentScore += points * 3
                    elif boardArray[int(locationX)][int(locationY)] == ' 3 ':
                        doubleWord = True
                    elif boardArray[int(locationX)][int(locationY)] == ' 4 ':
                        tripleWord = True

                    if doubleWord == True:
                        currentScore *= 2
                        turnScore += currentScore
                        currentScore = 0
                    elif tripleWord == True:
                        currentScore *= 3
                        turnScore += currentScore
                        currentScore = 0

                    score += turnScore
                    turnScore = 0

                    currentPlayer.score = score

                    boardArray[int(locationX)][int(locationY)] = ' ' + tilePlaced + ' '

                    for i in tileset:
                        if i == tilePlaced:
                            tileset = list(tileset)
                            tileset.remove(i)
                            
                            newTileset = ''
                            for j in tileset:
                                if j == ' ':
                                    continue

                                newTileset += j + ' '

                            tileset = newTileset

                            break

                    cli.sendall((f'TILES ' + tileset).encode(ENCODING))
                    cli.sendall((f'BOARDPUSH\n' + board.getBoard() + '\n').encode(ENCODING))
                    cli.sendall((f'TURN ' + currentPlayer.name).encode(ENCODING))
            elif 'EXCHANGE' in data and 'PLACE' not in data:
                splitData = data.split()

                if len(splitData) == 2:
                    for i in range(len(tileset)):
                        if tileset[i] == splitData[1]:
                            for j in tileset:
                                if j == splitData[1]:
                                    tileset = list(tileset)
                                    tileset.remove(j)
                                    
                                    newTileset = ''
                                    for k in tileset:
                                        if k == ' ':
                                            continue

                                        newTileset += k + ' '

                                    tileset = newTileset

                                    break

                            tileset += drawTiles(1)

                            cli.sendall((f'TILES ' + tileset).encode(ENCODING))
                            cli.sendall((f'BOARDPUSH\n' + board.getBoard() + '\n').encode(ENCODING))
                            cli.sendall((f'TURN ' + currentPlayer.name).encode(ENCODING))
                            break
                elif len(splitData) == 1:
                    tileset = drawTiles(7)

                    cli.sendall((f'TILES ' + tileset).encode(ENCODING))
                    cli.sendall((f'BOARDPUSH\n' + board.getBoard() + '\n').encode(ENCODING))
                    cli.sendall((f'TURN ' + currentPlayer.name).encode(ENCODING))

        if endTick == True:
            winner = players[0]

            for i in range(len(players)):
                if players[i].score > winner.score:
                    winner = players[i]

            cli.sendall((f'WINNER ' + str(winner.score) + ' ' + winner.name).encode(ENCODING))

            data = cli.recv(4096).decode(ENCODING)
            print(data)
            if 'QUIT' in data:
                cli.sendall(f'GOODBYE'.encode(ENCODING))

    break