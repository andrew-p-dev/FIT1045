def local_2_player_game():
    """
    Runs a local 2 player game of Connect 4.

    :return: None
    """
    # Implement your solution below
    print_board(board)
    #start from Player1:
    row = 0
    column = 0
    while board[row][column] == 0: #while there is a blank space
        if end_of_game(board) == 0:
            chosen_column = execute_player_turn(1,board)
            end_of_game(board) #checks if game over
            print_board(board) #prints the pretty board
            #test = validate_input(prompt, validate_inputs) #reassign column to player input
            print(f"Player 1 dropped a piece into column {chosen_column}") #print the column number that player dropped piece into
            if end_of_game(board) ==1:
                clear_screen()
                break
            elif end_of_game(board) ==2:
                clear_screen()
                break
            elif end_of_game(board) ==3:
                clear_screen()
                break
            chosen_column = execute_player_turn(2,board)
            end_of_game(board)
            print_board(board)
            print(f"Player 2 dropped a piece into column {chosen_column}")
            if end_of_game(board) ==1:
                clear_screen()
                break
            elif end_of_game(board) ==2:
                clear_screen()
                break
            elif end_of_game(board) ==3:
                clear_screen()
                break
        