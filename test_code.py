rows = 10
cols = 10
init_board = [[' ' for x in range(rows)]for y in range(cols)]
# print(init_board)

def formated_board_list(init_board): 
    for x in init_board:
        formated_board_string = '| ' + ' | '.join(x) + ' |'
        print(formated_board_string)
    print('')
formated_board_list(init_board)

items = ['apple', 'banana', 'cherry']
result = ' | '.join(items)
print(result)

# apple | banana | cherry

# output
# beginning: '| ' + ... + end: ' |'
# core: element + ' | ' + element (repeat)
# core: |_e_|_e_|_e_| ... |_e_|   
# the element keeps the position

# empty spots list 
empty_spots = [] # first it is completely empty
def reset_empty_spots_list(): 
    empty_spots.clear() # before the actutal game starts
    for row in range(rows): 
            for col in range (cols): 
                if init_board[row][col] == ' ':
                    empty_spots.append((row, col)) 
reset_empty_spots_list()

import random

num_bombs = 10 

# random bomb placement
for _ in range(num_bombs):
    row, col = random.choice(empty_spots) 
    init_board[row][col] = '*'
    empty_spots.remove((row, col))

formated_board_list(init_board)

# check surrounding spots
def check_bomb(init_board, row, col):
    base = 0 
    min_row = 0 
    max_row = 9
    min_col = 0
    max_col = 9
    

    # verticial check
    if min_row <= (row - 1) <= max_row: 
         if init_board[row - 1][col] == '*':
            base += 1 
    if min_row <= (row + 1) <= max_row: 
        if init_board[row + 1][col] == '*':
            base += 1 

    # horizontal check
    if min_col <= (col - 1) <= max_col: 
        if init_board[row][col - 1] == '*':
            base += 1 
    if min_col <= (col + 1) <= max_col: 
        if init_board[row][col + 1] == '*':
            base += 1 
    
    # diagonal check
    if min_row <= (row + 1) <= max_row and min_col <= (col - 1) <= max_col: 
        if init_board[row + 1][col - 1] == '*':
            base += 1 
    if min_row <= (row + 1) <= max_row and min_col <= (col + 1) <= max_col: 
        if init_board[row + 1][col + 1] == '*':
            base += 1 
    if min_row <= (row - 1) <= max_row and min_col <= (col - 1) <= max_col: 
        if init_board[row - 1][col - 1] == '*':
            base += 1 
    if min_row <= (row - 1) <= max_row and min_col <= (col + 1) <= max_col: 
        if init_board[row - 1][col + 1] == '*':
            base += 1 

    return str(base)


# nested loop 
for row in range(rows):
     for col in range(cols): 
          if init_board[row][col] != '*':
            value = check_bomb(init_board, row, col)
            init_board[row][col] = value

formated_board_list(init_board)


# game logic
# input user
    # row / col 
# check function
move = (row, col)

# valid move
def valid_move(user_board, move):
    row, col = move 

    # boarder check
    min_row = 0 
    max_row = 9
    min_col = 0
    max_col = 9
    if min_row <= row <= max_row and min_col <= col <= max_col: 
        return False

    # new move check
    if user_board[row][col] != ' ': 
        return False

    return True

def check_move(init_board, move):
    row, col = move 
    if init_board[row][col] == '*':
        return True 
    return False

# user board list
# update this with each move

# 0 check algo
# loop in a loop 
# super loop: iterates over the spots surrounding the user_move
    # sub loop: creating an interation each time a new 0-spot was discovered etc.
# add 0-spot to zero_checked_board when the 8 surrounding spot were checked
# no iterations on 0-spots that are in the zero_checked_board


