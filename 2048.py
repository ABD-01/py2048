from sys import exit
from os import system
import argparse
#from msvcrt import getch

# My own defined module consisting of functions such as transpose,inverse, print,etc
from essentials import *


# Checking for command line arguments with default board dimension 5x5 and default win criteria 2048
parser = argparse.ArgumentParser(description='Enter Board_Size and Win_criteria')
parser.add_argument('-n', '--size', type=int, default=5, help='Size of Board')
parser.add_argument('-w', '--win', type=int, default=2048, help='Win Criteria')
args = parser.parse_args()
board_size = args.size
win_cond = Powerof2(args.win)
##print("Win criteria is",win_cond)

# Initializing the board with all zeros and one 2 at random position
game_board = [[0]*board_size for _ in range(board_size)]
game_board = insert_two(game_board)
game_board = insert_two(game_board)
system('clear')
printboard(game_board)


# Check for input Key
def getKey():
    ch = getch().lower()
    while True:

        # checking if entered key is correct
        if ch in ['a', 's', 'd', 'w']:
            if isValid(ch, game_board) == False:
                print("Invalid move = ", ch)
                ch = getch().lower()
                continue
            else:
                ##print("You pressed", ch)
                return ch

        # If user wants to quit b/w gthe game
        elif ch == 'q':
            print("Do you want to Exit the game ?(y/n)")
            if input() in ['y', 'yes']:
                exit(1)
            else:
                printboard(game_board)
                ch = getch().lower()

        # In anyother case Re-propmt
        else:
            print("Invalid Key = ", ch)
            ch = getch().lower()
            continue


# Most Important part of the program
def game_move(ch, gboard):

    # Orienting the board so as all the actions are simply Left to Right
    if ch == 'd':
        board = gboard
    elif ch == 'a':
        board = invert(gboard)
    elif ch == 's':
        board = transpose(gboard)
    elif ch == 'w':
        board = transpose(gboard)
        board = invert(board)

    # Moving all Non-Zero elements to Rigth
    for row in board:
        row.sort(key=bool)

        #  merging two consecutive equal values
        i = len(row)-1
        while i >= 0:
            if row[i] == row[i-1]:
                row[i] = 2*row[i]
                row[i-1] = 0
                i -= 2
            else:
                i -= 1

    # Again moving all Non-zero elements to right
    for row in board:
        row.sort(key=bool)

    # Re-orienting the board back to the form it was
    if ch == 'w':
        board = invert(board)
        board = transpose(board)
    elif ch == 'a':
        board = invert(board)
    elif ch == 's':
        board = transpose(board)

    return board


# Similar to main function
while True:

    ch = getKey()
    system('clear')
    game_board = game_move(ch, game_board)
    game_board = insert_two(game_board)
    printboard(game_board)

    # Checking the game progress
    if didLose(game_board) == True:
        print('Game Over')
        exit(0)

    # checking for winning Criteria
    if any(win_cond in row for row in game_board) == True:
        print('You Win')
        exit(0)

