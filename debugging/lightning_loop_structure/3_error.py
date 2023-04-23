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
    if end_of_game() == 0:
        chosen_column = execute_player_turn()
        print_board()
        print(f"Player 1 dropped a piece into column {chosen_column}")
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
        