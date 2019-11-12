import socket
import sys
import random

global letter_points
letter_points = {"A":1, "B":3, "C":3, "D":2, "E":1, "F":4, "G":2, "H":4, "I":1, "J":1, "K":5, "L":1, "M":3, "N":1, "O":1, "P":3, "Q":10, "R":1, "S":1, "T":1, "U":1, "V":4, "W":4, "X":8, "Y":4, "Z":10}
class player:
    def __init__(self, bag):
        self.name = " "
        self.hand = hand(bag)
        self.score = 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_hand_str(self):
        return self.hand.get_hand_str()

    def get_hand_array(self):
        return self.hand.get_hand_array()

    def increase_score(self, increase):
        self.score += increase

    def get_score(self):
        return self.score
class bag:
    def __init__(self):
        self.bag = []
        self.initialize_bag()

    def add_to_bag(self, tile, amount):
        for i in range(amount):
            self.bag.append(tile)

    def initialize_bag(self):
        global letter_points
        self.add_to_bag(tiles(("A", letter_points), 9))
        self.add_to_bag(tiles(("B", letter_points), 2))
        self.add_to_bag(tiles(("C", letter_points), 2))
        self.add_to_bag(tiles(("D", letter_points), 4))
        self.add_to_bag(tiles(("E", letter_points), 12))
        self.add_to_bag(tiles(("F", letter_points), 2))
        self.add_to_bag(tiles(("G", letter_points), 3))
        self.add_to_bag(tiles(("H", letter_points), 2))
        self.add_to_bag(tiles(("I", letter_points), 9))
        self.add_to_bag(tiles(("J", letter_points), 9))
        self.add_to_bag(tiles(("K", letter_points), 1))
        self.add_to_bag(tiles(("L", letter_points), 4))
        self.add_to_bag(tiles(("M", letter_points), 2))
        self.add_to_bag(tiles(("N", letter_points), 6))
        self.add_to_bag(tiles(("O", letter_points), 8))
        self.add_to_bag(tiles(("P", letter_points), 2))
        self.add_to_bag(tiles(("Q", letter_points), 1))
        self.add_to_bag(tiles(("R", letter_points), 6))
        self.add_to_bag(tiles(("S", letter_points), 4))
        self.add_to_bag(tiles(("T", letter_points), 6))
        self.add_to_bag(tiles(("U", letter_points), 4))
        self.add_to_bag(tiles(("V", letter_points), 2))
        self.add_to_bag(tiles(("W", letter_points), 2))
        self.add_to_bag(tiles(("X", letter_points), 1))
        self.add_to_bag(tiles(("Y", letter_points), 2))
        self.add_to_bag(tiles(("Z", letter_points), 1))
        #self.add_to_bag(tiles((random())))
        shuffle(self.bag)

    def take_from_bag(self):
        return self.bag.pop()

    def get_remaining_tiles(self):
        return len(self.bag)
class Board:
     def __init__(self):
         self.board = [["   " for i in range(15)] for j in range(15)]
         self.add_multipliers()
         self.board[7][7] = " * "

     def get_board(self):
         board_str = "  |  " + "  |  ".join(str(item) for item in range(10, 15)) + " |"
         board_str += "\n _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
         board = list(self.board)
         for i in range(len(board)):
             if (i < 10):
                 board[i] = str(i) + "  | " + " | ".join(str(item) for item in board[i]) + " |"
             if (i >= 10):
                 board[i] = str(i) + " | " + " | ".join(str(item) for item in board[i]) + " |"
         board_str += "\n   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n".join(board)
         board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
         return board_str

     def add_prem_squares(self):
         Triple_Word = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
         Double_Word = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
         Triple_Letter = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
         Double_Letter = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

         for coordinate in Triple_Word:
             self.board[coordinate[0]][coordinate[1]] = "4"
         for coordinate in Triple_Letter:
             self.board[coordinate[0]][coordinate[1]] = "2"
         for coordinate in Double_Word:
             self.board[coordinate[0]][coordinate[1]] = "3"
         for coordinate in Double_Letter:
             self.board[coordinate[0]][coordinate[1]] = "1"

     def place(self, word, location, direction, player):
         global premium_spots
         premium_spots = []
         direction.lower()
         word = word.upper()

         if direction.lower() == "right":
             for i in range(len(word)):
                 if self.board[location[1]+1] != "   ":
                     premium_spots.append((word[i], self.board[location[0]][location[1]+i]))
                 self.board[location[0]][location[1]+i] = " " + word[i] + " "
         elif direction.lower() == "down":
             for i in range(len(word)):
                 if self.board[location[1]+1] != "   ":
                     premium_spots.append((word[i], self.board[location[0]][location[1]+i]))
                 self.board[location[0]][location[1]+i] = " " + word[i] + " "
         for letter in word:
             for tiles in player.get_hand_array():
                 if tiles.get_letter() == letter:
                     player.hand.remove_from_hand(tiles)
             player.hand.refill_hand()

class word:
    def __init__(self, word, location, player, direction, board):
        self.word = word.upper()
        self.location = location
        self.player = player
        self.direction = direction.lower()
        self.board = board

    #def check_word(self)

    def calculate_word_score(self):
        global letter_points, premium_spots
        premium_spots = []
        word_score = 0
        for letter in self.word:
            for spot in premium_spots:
                if letter == spot[0]:
                    if spot[1] == "TLS":
                        word_score += letter_points[letter] * 2
                    elif spot[2] == "DLS":
                        word_score += letter_points[letter]
            word_score += letter_points[letter]
        for spot in premium_spots:
            if spot[1] == "TWS":
                word_score *= 3
            elif spot[1] == "DWS":
                word_score *= 2
        self.player.increase_score(word_score)

    def set_word(self, word):
        self.word = word

    def set_location(self, location):
        self.location = Location

    def set_direction(self, direction):
        self.direction = direction

    def get_word(self):
        return self.word
class tiles:
    def __init__(self, letter, letter_points):
        self.letter = letter.upper()
        if self.letter in letter.upper():
            self.score = letter_points[self.letter]

        else:
            self.score = 0

    def get_letter(self):
        return self.letter

    def get_score(self):
        self.score

class hand:
    def __init__(self, bag):
        self.hand = []
        self.bag = bag
        self.initialize()

    def add_to_hand(self):
        self.hand.append(self.bag.take_from_bag())

    def initialize(self):
        for i in range(7):
            self.add_to_hand()

    def get_hand_str(self):
        return ", ".join(str(item.get_letter()) for item in self.hand)

    def get_hand_array(self):
        return self.hand

    def get_hand_length(self):
        return len(self.hand)

    def refill_hand(self):
        while self.get_hand_length() < 7 and self.bag.get_remaining_tiles() > 0:
            self.add_to_bag()
def turn(player, board, bag):
    global round_number, players, skipped_turns

    if (skipped_turns < 6) or (player.hand.get_hand_length() == 0 and bag.get_remaining_tiles() == 0):

        print("\nRound " + str(round_number) + ": " + player.get_name() + " 's turn \n")
        print(board.get_board())
        print("\n" + player.get_name() + "'s Hand: " + player.get_hand_str())

        word_to_play = input("Word to play: ")
        location = []
        col = input("Col num: ")
        row = input("row num: ")

        if(col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
            location = [-1, -1]
        else:
            location = [int(row), int(col)]
        direction = input("Direction of word (right or down): ")

        word = word(word_to_play, location, player, direction, board.board_array())

        if word.get_word() == "":
            print("your turn has been skipped.")

try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
except socket.error as err:
    print("The socket was not created")

port = 12345
host = '127.0.0.1'
global msg
global data
msg = ' '
ENCODING = 'ascii'
try:
    soc.bind((host, port))
    soc.listen(5)

    connection, address = soc.accept()
    print("socket binded to " + host + ":" + port)
except:
    print("The socket wasn't binded")

with connection:
    print("Conneted to ", address)

    counter = 0
    while True:
        while counter == 0:
            message = 'Hello'
            connection.sendall(bytes(message, ENCODING))
            data = connection.recv(2048)
            if not data:
                soc.close()

        # name_data = connection.recv(2048)
        # print("this is the initial name: " + name_data.decode()

            if "Hello" not in data.decode():
                print("Goodbye")
                break
            if "Hello" in data.decode():
                msg = "Ok: Scrabble server at your ready"
                connection.sendall(bytes(msg, ENCODING))

                name1_data = connection.recv(2048)
                print("this is the initial name: " + name1_data.decode())
                ok_name_message = "OK: the base name is set:  " + name1_data.decode()
                connection.sendall(bytes(ok_name_message, ENCODING))
                p1 = player(bag)
                pl.get_name(name1_data.decode())
                print(p1.get_name())
            else:
                break

            counter = 1

        data = connection.recv(2048)

        if "quit" in data.decode():
            msg = 'Goodbye'
            print("Goodbye")
            connection.send(bytes(msg, ENCODING))
            break

        elif "USERSET" in data.decode():
            connection.sendall(bytes("OK: USERSET is a viable command ", ENCODING))
            name_data = connection.recv(2048)
            print(name_data.decode())

            userchange = "Userchange " + name1_data.decode() + " has changed their name to " + name_data.decode()
            print(userchange)

        else:
            print("Goodbye")
            break

    soc.close()
