Values = {"A": 1,"B": 3, "C": 3,"D": 2,"E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 1,"K": 5, "L": 1, "M": 3, "N": 1,"O": 1, "P": 3,"Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4,"W": 4, "X": 8, "Y": 4,"Z": 10, "#": 0}

class Tiles:
    def __init__(self, letter, values):
        self.letter = letter.upper()
        if self.letter in values:
            self.score = values[self.letter]
        else:
            self.score = 0

    def GetLetter(self):
        return self.letter

    def GetScore(self):
        return self.score

class bag:
    def __init__(self):
        self.bag = []
        self.initialize_bag()

    def add_to_bag(self, tile, quantity):
        for i in range(quantity):
            self.bag.append(tile)

    def initialize_bag(self):
        global Values
        self.add_to_bag(Tiles("A", LETTER_VALUES), 9)
        self.add_to_bag(Tiles("B", LETTER_VALUES), 2)
        self.add_to_bag(Tiles("C", LETTER_VALUES), 2)
        self.add_to_bag(Tiles("D", LETTER_VALUES), 4)
        self.add_to_bag(Tiles("E", LETTER_VALUES), 12)
        self.add_to_bag(Tiles("F", LETTER_VALUES), 2)
        self.add_to_bag(Tiles("G", LETTER_VALUES), 3)
        self.add_to_bag(Tiles("H", LETTER_VALUES), 2)
        self.add_to_bag(Tiles("I", LETTER_VALUES), 9)
        self.add_to_bag(Tiles("J", LETTER_VALUES), 9)
        self.add_to_bag(Tiles("K", LETTER_VALUES), 1)
        self.add_to_bag(Tiles("L", LETTER_VALUES), 4)
        self.add_to_bag(Tiles("M", LETTER_VALUES), 2)
        self.add_to_bag(Tiles("N", LETTER_VALUES), 6)
        self.add_to_bag(Tiles("O", LETTER_VALUES), 8)
        self.add_to_bag(Tiles("P", LETTER_VALUES), 2)
        self.add_to_bag(Tiles("Q", LETTER_VALUES), 1)
        self.add_to_bag(Tiles("R", LETTER_VALUES), 6)
        self.add_to_bag(Tiles("S", LETTER_VALUES), 4)
        self.add_to_bag(Tiles("T", LETTER_VALUES), 6)
        self.add_to_bag(Tiles("U", LETTER_VALUES), 4)
        self.add_to_bag(Tiles("V", LETTER_VALUES), 2)
        self.add_to_bag(Tiles("W", LETTER_VALUES), 2)
        self.add_to_bag(Tiles("X", LETTER_VALUES), 1)
        self.add_to_bag(Tiles("Y", LETTER_VALUES), 2)
        self.add_to_bag(Tiles("Z", LETTER_VALUES), 1)
        self.add_to_bag(Tiles("#", LETTER_VALUES), 2)
        shuffle(self.bag)

    def take_from_bag(self):
        return self.bag.pop()

    def get_remaining_tiles(self):
        return len(self.bag)


class Hand:
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
        return ", ".join(str(item.get_letter() for item in self.hand))

    def get_hand_array(self):
        return self.hand

    def get_hand_length(self):
        return len(self.hand)

    def remove_from_hand(self, tile):
        self.hand.remove(tile)

    def refill_hand(self):
        while self.get_hand_length() < 7 and self.bag.get_remaining_tiles() > 0:
            self.add_to_hand()

class Player:
    def __init__(self, bag):
        self.name = ""
        self.hand = Hand(bag)
        self.score = 0

    def set_name(self, name):
        self.name = name

    def get_hand_str(self):
        return self.hand.get_hand_str()

    def get_hand_array(self):
        return self.hand.get_hand_array()

    def score(self, increase):
        self.score += increase

    def GetScore(self):
        return self.score

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

    def check_word(self):
        global round_number, players
        word_score = 0
        dictionary = open(" ").read()
