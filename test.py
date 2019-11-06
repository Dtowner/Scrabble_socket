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
        def __init__(self, word, location, player, direction, board):
        self.word = word.upper()
        self.location = location
        self.player = player
        self.direction = direction.lower()
        self.board = board

    def check_word(self):
        #Checks the word to make sure that it is in the dictionary, and that the location falls within bounds.
        #Also controls the overlapping of words.
        global round_number, players
        word_score = 0
        dictionary = open("dic.txt").read()

        current_board_ltr = ""
        needed_tiles = ""
        blank_tile_val = ""

        #Assuming that the player is not skipping the turn:
        if self.word != "":

            #Allows for players to declare the value of a blank tile.
            if "#" in self.word:
                while len(blank_tile_val) != 1:
                    blank_tile_val = input("Please enter the letter value of the blank tile: ")
                self.word = self.word[:word.index("#")] + blank_tile_val.upper() + self.word[(word.index("#")+1):]

            #Reads in the board's current values under where the word that is being played will go. Raises an error if the direction is not valid.
            if self.direction == "right":
                for i in range(len(self.word)):
                    if self.board[self.location[0]][self.location[1]+i][1] == " " or self.board[self.location[0]][self.location[1]+i] == "TLS" or self.board[self.location[0]][self.location[1]+i] == "TWS" or self.board[self.location[0]][self.location[1]+i] == "DLS" or self.board[self.location[0]][self.location[1]+i] == "DWS" or self.board[self.location[0]][self.location[1]+i][1] == "*":
                        current_board_ltr += " "
                    else:
                        current_board_ltr += self.board[self.location[0]][self.location[1]+i][1]
            elif self.direction == "down":
                for i in range(len(self.word)):
                    if self.board[self.location[0]+i][self.location[1]] == "   " or self.board[self.location[0]+i][self.location[1]] == "TLS" or self.board[self.location[0]+i][self.location[1]] == "TWS" or self.board[self.location[0]+i][self.location[1]] == "DLS" or self.board[self.location[0]+i][self.location[1]] == "DWS" or self.board[self.location[0]+i][self.location[1]] == " * ":
                        current_board_ltr += " "
                    else:
                        current_board_ltr += self.board[self.location[0]+i][self.location[1]][1]
            else:
                return "Error: please enter a valid direction."

            #Raises an error if the word being played is not in the official scrabble dictionary (dic.txt).
            if self.word not in dictionary:
                return "Please enter a valid dictionary word.\n"

            #Ensures that the words overlap correctly. If there are conflicting letters between the current board and the word being played, raises an error.
            for i in range(len(self.word)):
                if current_board_ltr[i] == " ":
                    needed_tiles += self.word[i]
                elif current_board_ltr[i] != self.word[i]:
                    print("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + self.word + ", Needed_Tiles: " + needed_tiles)
                    return "The letters do not overlap correctly, please choose another word."

            #If there is a blank tile, remove it's given value from the tiles needed to play the word.
            if blank_tile_val != "":
                needed_tiles = needed_tiles[needed_tiles.index(blank_tile_val):] + needed_tiles[:needed_tiles.index(blank_tile_val)]

            #Ensures that the word will be connected to other words on the playing board.
            if (round_number != 1 or (round_number == 1 and players[0] != self.player)) and current_board_ltr == " " * len(self.word):
                print("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + self.word + ", Needed_Tiles: " + needed_tiles)
                return "Please connect the word to a previously played letter."

            #Raises an error if the player does not have the correct tiles to play the word.
            for letter in needed_tiles:
                if letter not in self.player.get_rack_str() or self.player.get_rack_str().count(letter) < needed_tiles.count(letter):
                    return "You do not have the tiles for this word\n"

            #Raises an error if the location of the word will be out of bounds.
            if self.location[0] > 14 or self.location[1] > 14 or self.location[0] < 0 or self.location[1] < 0 or (self.direction == "down" and (self.location[0]+len(self.word)-1) > 14) or (self.direction == "right" and (self.location[1]+len(self.word)-1) > 14):
                return "Location out of bounds.\n"

            #Ensures that first turn of the game will have the word placed at (7,7).
            if round_number == 1 and players[0] == self.player and self.location != [7,7]:
                return "The first turn must begin at location (7, 7).\n"
            return True

        #If the user IS skipping the turn, confirm. If the user replies with "Y", skip the player's turn. Otherwise, allow the user to enter another word.
        else:
            if input("Are you sure you would like to skip your turn? (y/n)").upper() == "Y":
                return True
            else:
                return "Please enter a word."

    def calculate_word_score(self):
        #Calculates the score of a word, allowing for the impact by premium squares.
        global LETTER_VALUES, premium_spots
        premium_spots = []
        word_score = 0
        for letter in self.word:
            for spot in premium_spots:
                if letter == spot[0]:
                    if spot[1] == "TLS":
                        word_score += LETTER_VALUES[letter] * 2
                    elif spot[2] == "DLS":
                        word_score += LETTER_VALUES[letter]
            word_score += LETTER_VALUES[letter]
        for spot in premium_spots:
            if spot[1] == "TWS":
                word_score *= 3
            elif spot[1] == "DWS":
                word_score *= 2
        self.player.increase_score(word_score)

    def set_word(self, word):
        self.word = word

    def set_location(self, location):
        self.location = location

    def set_direction(self, direction):
        self.direction = direction

    def get_word(self):
        return self.word

def turn(player, board, bag):
    #Begins a turn, by displaying the current board, getting the information to play a turn, and creates a recursive loop to allow the next person to play.
    global round_number, players, skipped_turns

    #If the number of skipped turns is less than 6 and a row, and there are either tiles in the bag, or no players have run out of tiles, play the turn.
    #Otherwise, end the game.
    if (skipped_turns < 6) or (player.rack.get_rack_length() == 0 and bag.get_remaining_tiles() == 0):

        #Displays whose turn it is, the current board, and the player's rack.
        print("\nRound " + str(round_number) + ": " + player.get_name() + "'s turn \n")
        print(board.get_board())
        print("\n" + player.get_name() + "'s Letter Rack: " + player.get_rack_str())

        #Gets information in order to play a word.
        word_to_play = input("Word to play: ")
        location = []
        col = input("Column number: ")
        row = input("Row number: ")
        if (col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
            location = [-1, -1]
        else:
            location = [int(row), int(col)]
        direction = input("Direction of word (right or down): ")

        word = Word(word_to_play, location, player, direction, board.board_array())

        #If the first word throws an error, creates a recursive loop until the information is given correctly.
        while word.check_word() != True:
            print (word.check_word())
            word.set_word(input("Word to play: "))
            location = []
            col = input("Column number: ")
            row = input("Row number: ")
            if (col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
                location = [-1, -1]
            else:
                word.set_location([int(row), int(col)])
            word.set_direction(input("Direction of word (right or down): "))

        #If the user has confirmed that they would like to skip their turn, skip it.
        #Otherwise, plays the correct word and prints the board.
        if word.get_word() == "":
            print("Your turn has been skipped.")
            skipped_turns += 1
        else:

            board.place_word(word_to_play, location, direction, player)
            word.calculate_word_score()
            skipped_turns = 0

        #Prints the current player's score
        print("\n" + player.get_name() + "'s score is: " + str(player.get_score()))

        #Gets the next player.
        if players.index(player) != (len(players)-1):
            player = players[players.index(player)+1]
        else:
            player = players[0]
            round_number += 1

        #Recursively calls the function in order to play the next turn.
        turn(player, board, bag)

    #If the number of skipped turns is over 6 or the bag has both run out of tiles and a player is out of tiles, end the game.
    else:
        end_game()

def start_game():
    #Begins the game and calls the turn function.
    global round_number, players, skipped_turns
    board = Board()
    bag = Bag()

    #Asks the player for the number of players.
    num_of_players = int(input("\nPlease enter the number of players (2-4): "))
    while num_of_players < 2 or num_of_players > 4:
        num_of_players = int(input("This number is invalid. Please enter the number of players (2-4): "))

    #Welcomes players to the game and allows players to choose their name.
    print("\nWelcome to Scrabble! Please enter the names of the players below.")
    players = []
    for i in range(num_of_players):
        players.append(Player(bag))
        players[i].set_name(input("Please enter player " + str(i+1) + "'s name: "))

    #Sets the default value of global variables.
    round_number = 1
    skipped_turns = 0
    current_player = players[0]
    turn(current_player, board, bag)

def end_game():
    #Forces the game to end when the bag runs out of tiles.
    global players
    highest_score = 0
    winning_player = ""
    for player in players:
        if player.get_score > highest_score:
            highest_score = player.get_score()
            winning_player = player.get_name()
    print("The game is over! " + player.get_name() + ", you have won!")

    if input("\nWould you like to play again? (y/n)").upper() == "Y":
        start_game()

start_game()

    
