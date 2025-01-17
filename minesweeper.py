import random

# init board
# first focus on the empty spots
# 10x10 
rows = 10
cols = 10
init_board = [[' ' for x in range(rows)]for y in range(cols)]

# formated board
def formated_board_list(init_board): 
    for x in init_board:
        formated_board_string = '| ' + ' | '.join(x) + ' |'
        print(formated_board_string)
    print('')

# empty spots list 
empty_spots = [] 
def reset_empty_spots_list(): 
    empty_spots.clear() 
    for row in range(rows): 
            for col in range (cols): 
                if init_board[row][col] == ' ':
                    empty_spots.append((row, col)) 

# planting bombs
# like a random computer player choicing a spot between all empty spots
num_bombs = 10 
for _ in range(num_bombs):
    row, col = random.choice(empty_spots) 
    init_board[row][col] = '*'
    empty_spots.remove((row, col))

# neighbor counting
# loop through each cell
# check of neighboring bombs
# if true >> count +1 
# use a nested loop
# depared the alorithms in diverse methods
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

# game logic: win/loss 
# create user_board
    # here he sees all what he has discovered

# game loop 
# game starts
reset_empty_spots_list()

# end
formated_board_list(init_board) # revealing the init_board