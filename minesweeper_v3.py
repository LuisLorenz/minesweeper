import random
import copy

rows = 10
cols = 10
init_board = [[' ' for x in range(rows)] for y in range(cols)]
# user_board
user_board = copy.deepcopy(init_board)

def reset_board(board): # try out if this works
    board.clear()
    return board

# formated board
def formated_board_list(board): 
    for x in board:
        formated_board_string = '| ' + ' | '.join(x) + ' |'
        print(formated_board_string)
    print('')

# Generate list of empty spots
def reset_empty_spots_list():
    return [(row, col) for row in range(rows) for col in range(cols) if init_board[row][col] == ' ']

# Plant bombs on the board
def plant_bombs():
    empty_spots = reset_empty_spots_list()
    num_bombs = 10
    
    # if num_bombs > len(empty_spots):
    #     raise ValueError("Not enough empty spots to place all bombs!")

    for _ in range(num_bombs):
        row, col = random.choice(empty_spots)
        init_board[row][col] = '*'
        empty_spots.remove((row, col))

    return empty_spots

def check_neighbor_bombs(init_board, row, col):
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

    return str(base) # the values in the grid are all strings

def assign_board(): 
    # nested loop 
    for row in range(rows):
        for col in range(cols): 
            if init_board[row][col] != '*':
                value = check_neighbor_bombs(init_board, row, col)
                init_board[row][col] = value

# valid_move
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
        pass
    else:
        print('This field is not in the play board. Please try again.')
        return False

    # new move check
    if user_board[row][col] != ' ': 
        print('This field has already been dug. Please choose a different one.')
        return False

    return True

def check_bomb(init_board, move):
    row, col = move 
    if init_board[row][col] == '*':
        return True 
    return False

def eight_spot_check(init_board, user_board, move): 
    row, col = move 

    # defining the boarders
    # min_row = 0 
    # max_row = 9
    # min_col = 0
    # max_col = 9

    min_row, max_row = 0, len(init_board) - 1
    min_col, max_col = 0, len(init_board[0]) - 1

     # List all eight possible directions
    directions = [
        (-1, 0),  # top
        (-1, -1), # top-left
        (0, -1),  # left
        (1, -1),  # bottom-left
        (1, 0),   # bottom
        (1, 1),   # bottom-right
        (0, 1),   # right                                                   
        (-1, 1)   # top-right
    ]

    # Use a queue for BFS
    queue = [move]
    visited = set(queue) # 

    while queue:
        current_row, current_col = queue.pop(0) #
            # so the first move at index '0' is removed
            # avoiding a repetition this way
        user_board[current_row][current_col] = init_board[current_row][current_col]

        # If the current cell is '0', explore its neighbors
        if init_board[current_row][current_col] == '0':
            for dr, dc in directions: # direction row, direction col
                # each tuple is used 
                new_row, new_col = current_row + dr, current_col + dc

                # Check boundaries
                if min_row <= new_row <= max_row and min_col <= new_col <= max_col:
                    if (new_row, new_col) not in visited and user_board[new_row][new_col] == ' ':
                        user_board[new_row][new_col] = init_board[new_row][new_col] # it is impossible to reveal a '*' with this 
                        visited.add((new_row, new_col)) # so the coordinates are saved, tracking queue 

                        # Add to queue if the new cell is also a '0'
                        if init_board[new_row][new_col] == '0':
                            queue.append((new_row, new_col))

        # for the move all the surrounding spots are checked
        #   therefore all the numbers are added
        #   if the number is 0 the coordinates run the queue like move 

def is_win(init_board, user_board):
    # all none bomb spots are revealed 
    # it is about the user_board
    # opt 1: interate through the whole board and see if there are still spots that are ' ' and are not '*' in compariation with the init_board
    # if False: win 
    for r in range(rows):
        for c in range(cols): 
            if user_board[r][c] == ' ':
                if init_board[r][c] != '*':
                    return False
    return True
            
def intro():
    print('Welcome to MINESWEEPER.')

# game logic: win/loss
def game(init_board, user_board):
    while True: 
        

        plant_bombs()
        assign_board()

        # show current board
        formated_board_list(user_board)

        # get user move
        while True: 
            print('Where do you want to dig?')
            move_row = input('Row = ')
            move_col = input('Col = ')
            move = (move_row, move_col)
            if valid_move(user_board, move) == True:
                row = int(move_row) 
                col = int(move_col)
                move =(row, col)
                break
        
        # check move
        if check_bomb(init_board, move) == True: 
            print('You dug into a bomb!')
            formated_board_list(init_board)
            break

        user_board[row][col] = init_board[row][col]
        # spot to 0, 1, 2, 3 etc. 

        if init_board[row][col] == '0':
            eight_spot_check(init_board, user_board, move) # here implement the 0 revelation algo

        # check for win
        if is_win(init_board, user_board) == True:
            print('You revealed spotted all the bombs. Congrates.')
            formated_board_list(init_board)
            break

# # check move
# if check_move(move) == True:
#     print('You hit a bomb.')
#     formated_board_list(init_board)
#     break 

intro()
# game loop 
# game starts
while True:
    game(init_board, user_board)
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

        