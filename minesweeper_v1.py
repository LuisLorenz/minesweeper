import random

# init board
# first focus on the empty spots
# 10x10 
rows = 10
cols = 10
init_board = [[' ' for x in range(rows)]for y in range(cols)]

# user_board
user_board = init_board 

# zero_spots_board
zero_checked_board = init_board

# formated board
def formated_board_list(board): 
    for x in board:
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
    # top mid
    if min_row <= (row - 1) <= max_row: 
         if init_board[row - 1][col] == '*':
            base += 1 
    
    # bottom mid
    if min_row <= (row + 1) <= max_row: 
        if init_board[row + 1][col] == '*':
            base += 1 

    # horizontal check
    # mid left
    if min_col <= (col - 1) <= max_col: 
        if init_board[row][col - 1] == '*':
            base += 1 
    
    # mid right 
    if min_col <= (col + 1) <= max_col: 
        if init_board[row][col + 1] == '*':
            base += 1 
    
    # diagonal check
    # bottom left
    if min_row <= (row + 1) <= max_row and min_col <= (col - 1) <= max_col: 
        if init_board[row + 1][col - 1] == '*':
            base += 1

    # bottom right
    if min_row <= (row + 1) <= max_row and min_col <= (col + 1) <= max_col: 
        if init_board[row + 1][col + 1] == '*':
            base += 1 
    
    # top left
    if min_row <= (row - 1) <= max_row and min_col <= (col - 1) <= max_col: 
        if init_board[row - 1][col - 1] == '*':
            base += 1 
    
    # top right 
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

# user_board

# valid_move
    # in range of boards
    # in empthy spots
        # here the board is equal to the user_board-
def valid_move(user_board, move):
    row, col = move 

    try: 
        row = int(row) 
        col = int(col)
    except ValueError: 
        print('Your input was invalid. Please insert numbers between 0 to 9.')

    # boarder check
    min_row = 0 
    max_row = 9
    min_col = 0
    max_col = 9
    if min_row <= row <= max_row and min_col <= col <= max_col: 
        print('This field is not in the play board. Please try again.')
        return False

    # new move check
    if user_board[row][col] != ' ': 
        print('This field has already been dug. Please choose a different one.')
        return False

    return True

def check_move(init_board, move):
    row, col = move 
    if init_board[row][col] == '*':
        return True 
    return False

# def eight_spot_check(init_board, user_board, move): 
    # algo checks all surroundning spots if there are any futher 0 spots
    # should only run if the user spot was a 0-spot
    # to avoid running this algo in circle all the time, 
    # I have to save all the 0-spots 
    # which surrounding spots were already checked
    # 'zero_checked_board'
    min_row = 0 
    max_row = 9
    min_col = 0
    max_col = 9
    
    # # update user_board
    # user_board[row][col] = init_board[row][col]

    # top mid
    if min_row <= (row - 1) <= max_row: 
        if user_board[row - 1][col] == ' ':  
            if init_board[row - 1][col] == '0':
                user_board[row - 1][col] = init_board[row - 1][col]
        
    # top left
    if min_row <= (row - 1) <= max_row and min_col <= (col - 1) <= max_col: 
        if user_board[row - 1][col] == ' ':     
            if init_board[row - 1][col - 1] == '0':
                user_board[row - 1][col - 1] = init_board[row - 1][col - 1]
    
    # mid left
    if min_col <= (col - 1) <= max_col:
        if user_board[row - 1][col] == ' ': 
            if init_board[row][col - 1] == '0':
                user_board[col - 1] = init_board[col - 1]
    
    # bottom left
    if min_row <= (row + 1) <= max_row and min_col <= (col - 1) <= max_col: 
        if user_board[row - 1][col] == ' ': 
            if init_board[row + 1][col - 1] == '0':
                user_board[row + 1][col - 1] = init_board[row + 1][col - 1]
    
    # bottom mid
    if min_row <= (row + 1) <= max_row:
        if user_board[row - 1][col] == ' ': 
            if init_board[row + 1][col] == '0':
                user_board[row + 1][col] = init_board[row + 1][col]
    
    # bottom right
    if min_row <= (row + 1) <= max_row and min_col <= (col + 1) <= max_col: 
        if user_board[row - 1][col] == ' ': 
            if init_board[row + 1][col + 1] == '0':
                user_board[row + 1][col + 1] = init_board[row + 1][col + 1]
    
    # mid right
    if min_col <= (col + 1) <= max_col: 
        if user_board[row - 1][col] == ' ': 
            if init_board[row][col + 1] == '0':
                user_board[row][col + 1] = init_board[row][col + 1]
    
    # top right 
    if min_row <= (row - 1) <= max_row and min_col <= (col + 1) <= max_col:
        if user_board[row - 1][col] == ' ': 
            if init_board[row - 1][col + 1] == '0':
                user_board[row - 1][col + 1] = init_board[row - 1][col + 1]

    # add main spot to zero_checked_board


def eight_spot_check(init_board, user_board, move): 
    row, col = move 

    min_row = 0 
    max_row = 9
    min_col = 0
    max_col = 9

    # top mid
    if min_row <= (row - 1) <= max_row: 
        if user_board[row - 1][col] == ' ':  
            if init_board[row - 1][col] == '0':
                user_board[row - 1][col] = init_board[row - 1][col]
                sub_move = (row - 1, col)
                eight_spot_check(init_board, user_board, sub_move)
        
    # top left
    if min_row <= (row - 1) <= max_row and min_col <= (col - 1) <= max_col: 
        if user_board[row - 1][col] == ' ':     
            if init_board[row - 1][col - 1] == '0':
                user_board[row - 1][col - 1] = init_board[row - 1][col - 1]
                sub_move = (row - 1, col)
                eight_spot_check(init_board, user_board, sub_move)
    
    # mid left
    if min_col <= (col - 1) <= max_col:
        if user_board[row - 1][col] == ' ': 
            if init_board[row][col - 1] == '0':
                user_board[col - 1] = init_board[col - 1]
                sub_move = (row - 1, col)
                eight_spot_check(init_board, user_board, sub_move)
    
    # bottom left
    if min_row <= (row + 1) <= max_row and min_col <= (col - 1) <= max_col: 
        if user_board[row - 1][col] == ' ': 
            if init_board[row + 1][col - 1] == '0':
                user_board[row + 1][col - 1] = init_board[row + 1][col - 1]
                sub_move = (row - 1, col)
                eight_spot_check(init_board, user_board, sub_move)
    
    # bottom mid
    if min_row <= (row + 1) <= max_row:
        if user_board[row - 1][col] == ' ': 
            if init_board[row + 1][col] == '0':
                user_board[row + 1][col] = init_board[row + 1][col]
                sub_move = (row - 1, col)
                eight_spot_check(init_board, user_board, sub_move)
    
    # bottom right
    if min_row <= (row + 1) <= max_row and min_col <= (col + 1) <= max_col: 
        if user_board[row - 1][col] == ' ': 
            if init_board[row + 1][col + 1] == '0':
                user_board[row + 1][col + 1] = init_board[row + 1][col + 1]
                sub_move = (row - 1, col)
                eight_spot_check(init_board, user_board, sub_move)
    
    # mid right
    if min_col <= (col + 1) <= max_col: 
        if user_board[row - 1][col] == ' ': 
            if init_board[row][col + 1] == '0':
                user_board[row][col + 1] = init_board[row][col + 1]
                sub_move = (row - 1, col)
                eight_spot_check(init_board, user_board, sub_move)
    
    # top right 
    if min_row <= (row - 1) <= max_row and min_col <= (col + 1) <= max_col:
        if user_board[row - 1][col] == ' ': 
            if init_board[row - 1][col + 1] == '0':
                user_board[row - 1][col + 1] = init_board[row - 1][col + 1]
                sub_move = (row - 1, col)
                eight_spot_check(init_board, user_board, sub_move)

# def neighbor_count(init_board, user_board, move):
    # min_row = 0 
    # max_row = 9
    # min_col = 0
    # max_col = 9
    
    # # update user_board
    # user_board[row][col] = init_board[row][col]

    while True: 

    # this is algo is not necessary anymore?

    # implement a method that check once around all the 8 spots
        # copy = user_board
        if init_board[row - 1][col] == '0':
            user_board[row - 1][col] = init_board[row - 1][col]
        if init_board[row - 1][col - 1] == '0':
            user_board[row - 1][col - 1] = init_board[row - 1][col - 1]
        if init_board[row][col - 1] == '0':
            user_board[col - 1] = init_board[col - 1]
        if init_board[row + 1][col - 1] == '0':
            user_board[row + 1][col - 1] = init_board[row + 1][col - 1]
        if init_board[row + 1][col] == '0':
            user_board[row + 1][col] = init_board[row + 1][col]
        if init_board[row + 1][col + 1] == '0':
            user_board[row + 1][col + 1] = init_board[row + 1][col + 1]
        if init_board[row][col + 1] == '0':
            user_board[row][col + 1] = init_board[row][col + 1]
        if init_board[row - 1][col + 1] == '0':
            user_board[row - 1][col + 1] = init_board[row - 1][col + 1]
        # if copy == user_board:
            # nothing has changed >> alorithm can stop
                # first the algorithim needs to run from every surrounding spot 

def intro():
    print('Welcome to MINESWEEPER.')

# game logic: win/loss
def game():
    while True: 
        # show current board
        formated_board_list(user_board)




        break
    # end
    formated_board_list(init_board) # revealing the init_board



# getting valid user_move
    while True: 
        'Where do you want to dig?'
        move_row = input('Row = ')
        move_col = input('Col = ')
        move = (move_row, move_col)
        if valid_move(move) == True:
            break

# check move
# if check_move(move) == True:
#     print('You hit a bomb.')
#     formated_board_list(init_board)
#     break 



user_board[row][col] = init_board[row][col]
# spot to 0, 1, 2, 3 etc. 

if init_board[row][col] == '0':
    eight_spot_check(move) # here implement the 0 revelation algo

# else:
#     user_board[row][col] = init_board[row][col] 

# create user_board
    # here he sees all what he has discovered

intro()
# game loop 
# game starts
while True:
    reset_empty_spots_list()
    game()
    while True:
        play_again = input('Do you want play again? (y/n)')
        try: 
            if play_again == 'y' or play_again == 'n':
                break
            else:
                print("Please insert 'y' or 'n'.")
        except ValueError:
            print('Please insert a string.')

    if play_again == 'n':
        break

        