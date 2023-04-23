from os import name, system

def clear_screen():
    system('cls' if name == 'nt' else 'clear')

# just print something so we can see how print_board and clear_screen interact
def print_board():
    print("BOARD")

# use this variable to control whether the game is over
isEndOfGame = False
def end_of_game():
    return 1 if isEndOfGame else 0

# always drop a piece in the first column
def execute_player_turn():
    return 1 

def local_2_player_game():
    print_board()
    row = 0
    column = 0
    # This while loop is problematic
    # while board[row][column] == 0:
    if end_of_game() == 0:
        chosen_column = execute_player_turn()
        end_of_game() #checks if game over
        print_board() #prints the pretty board
        #test = validate_input(prompt, validate_inputs) #reassign column to player input
        print(f"Player 1 dropped a piece into column {chosen_column}") #print the column number that player dropped piece into
        if end_of_game() == 1:
            clear_screen()
            return
        elif end_of_game() == 2:
            clear_screen()
            return
        elif end_of_game() == 3:
            clear_screen()
            return
        chosen_column = execute_player_turn()
        end_of_game()
        print_board()
        print(f"Player 2 dropped a piece into column {chosen_column}")
        if end_of_game() == 1:
            clear_screen()
            return
        elif end_of_game() == 2:
            clear_screen()
            return
        elif end_of_game() == 3:
            clear_screen()
            return
        