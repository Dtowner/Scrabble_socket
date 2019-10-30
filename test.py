import string
import random

#string.ascii_letters
#random.choice(string.ascii_letters)
# initial_hand_size = 7
# for i in range(7):
#     l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#     x = l[random.randint(0,25)]
#     print(x)

# def tiles(initial_hand_size):
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(initial_hand_size))
#
# print(tiles(7))
# def userset()
#
#
#
# def turn(user_number):
#     switcher = {
#     1: "player1",
#     2: "player2",
#     3: "player3",
#     4: "player4",
#     }
#     return switcher.get(user_number)
#
# print(turn(player2))

board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]

board[1][1] = 'a'
for count, row in enumerate(board):
    print(count, row)

board[1][1] = 'a'
