def validate_input(prompt, valid_inputs):
	while True:
		try:
			user_input = str(input(f"{prompt}"))
			for i in range(len(valid_inputs)):
				if user_input == valid_inputs[i]:
					return user_input
			else:
				print("Invalid input, please try again.")
		except ValueError:
			print("Invalid input, please try again.")
	
board = []

def create_board():
	connect4_board = []
	initial = ' '
	connect_columns = [initial, initial, initial, initial, initial, initial, initial] # we are gonna have 7 columns
	connect_rows = [initial, initial, initial, initial, initial, initial] ## we are gonna have 6 rows
	length_rows = len(connect_rows)
	length_columns = len(connect_columns)
	
	for i in range(length_rows):
		connect4_board.append([])
		for j in range(length_columns):
			connect4_board[i].append(' ')
	return connect4_board

def print_board(connect4_board):
	number_rows = 6
	number_columns = 7

	#This is the start of printing our connect 4 board to the terminal.
	print("========== Connect4 =========")
	print("Player 1: X       Player 2: O\n")
	print("  1   2   3   4   5   6   7")

	for a in range(number_rows):
		print(" --- --- --- --- --- --- ---") #prints this boundary first in the 0th,1st,2nd row etc.
		print("|", end ="") #the end function joins strings together. If i add end="" with no space, it will stay on the same line
							#makes the print function stay on the same line
							#Usually, a normal print function will automatically go to the next line
							
		for b in range(number_columns):
			#If the current box we are on is a piece =1 then =X	
			if connect4_board[a][b] == 'X': 
				connect4_board[a][b] = "X"
				#Then we print the "X" and leave a " |" afterwards
				#The space at the start was just there to try allign everything up (trial n error)
				print(f" {connect4_board[a][b]}", end=" |")	

			elif	connect4_board[a][b] == 'O':
				connect4_board[a][b] = "O"
				#Then we print the "O" and leave a " |" afterwards and a space at the start
				#The space at the start was just there to try allign everything up (trial n error)
				print(f" {connect4_board[a][b]}", end=" |")

			elif connect4_board[a][b] == ' ':
				connect4_board[a][b] = " "
				#Then we print the " " and leave a " |" afterwards
				#The space at the start was just there to try allign everything up (trial n error)
				print(f" {connect4_board[a][b]}", end=" |")
			else:
				print()
				for row in connect4_board:
					print(row)
				raise Exception(f"There was some unexpected character \"{connect4_board[a][b]}\" at [{a}][{b}]")
		print("")
	
	print(" --- --- --- --- --- --- ---")
	print("=============================")

def drop_piece(connect4_board, player, column):
	column -= 1 
	if player == 1:
		for m in reversed(range(0,6)):
			if connect4_board[m][column] == " ":
				connect4_board[m][column] = 'X'
				print("We set it to X and returned True")
				return True
			elif (connect4_board[m][column] == 'X') or (connect4_board[m][column] == 'O'):
				return False
	elif player == 2:
		for n in reversed(range(0,6)):
			if connect4_board[n][column] == ' ':
				print("We set it to O and returned True")
				connect4_board[n][column] = 'O'
				return True
			elif (connect4_board[n][column] == 'X') or (connect4_board[n][column] == 'O'):
				return False
	
def execute_player_turn(player, board): # Task 5
	prompt = f"Player {player}, please enter the column you would like to drop your piece into: "

	while True:
		valid_inputs = ["1", "2", "3", "4", "5", "6", "7"]
		#Call the function from task 1:
		column_input = int(validate_input(prompt, valid_inputs))

		selected_drop = drop_piece(board, player, column_input)

		print(column_input)
		if selected_drop == True:
			return column_input
				
		elif selected_drop == False:
			print("That column is full, please try again.")
			break
		else:
			print("Error. Please try again.")
			break

def end_of_game(board): # Question 6
	rows = len(board)  #6 rows
	columns = len(board[0]) #7 columns

	#CHECKING VERTICALLY:
	for i in reversed(range(0,columns)): #looping through the COLUMNS
		for j in reversed(range(0,rows-3)): #looping through the ROWS

			#To measure vertically for positive slope, we need to add one to the row everytime but stay in the current column.

			#If the player is player 1:
			if board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i] == 'X':
				return 1	
			#If the player is player 2:
			elif board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i] == 'O':
				return 2
	#CHECKING HORIZONTALLY:
	for i in reversed(range(0,columns-3)): 

		for j in reversed(range(0,rows)):
		
			#If the player is player 1:

			if board[j][i] == board[j][i+1] == board[j][i+2] == board[j][i+3] == 'X':
				return 1
			#If the player is player 2:

			elif board[j][i] == board[j][i+1] == board[j][i+2] == board[j][i+3] == 'O':
			
				return 2
	#NEGATIVE GRADIENT
	for i in range(0, columns - 3): 
		for j in range(3, rows): 
			if board[j][i] == board[j-1][i+1] == board[j-2][i+2] == board[j-3][i+3] == 'X':
				return 1
			elif board[j][i] == board[j-1][i+1] == board[j-2][i+2] == board[j-3][i+3] == 'O':
				return 2

	#POSITIVE GRADIENT
	for i in range(0, columns - 3): 

		for j in range(0, rows - 3): 

			if board[j][i] == board[j+1][i+1] == board[j+2][i+2] == board[j+3][i+3] == 'X':
				return 1

			elif board[j][i] == board[j+1][i+1] == board[j+2][i+2] == board[j+3][i+3] == 'O':
				return 2
	counter = 0
	# Lets say the board was 6x7. That means there are 6x7 =42 spaces on the board
	# If the counter reaches 42, that means the board is filled = game over.
	max_counter = rows * columns

	#Checking if it is a draw or not
	for i in reversed(range(0,rows)):
		for j in reversed(range(0,columns)):
			
			if (board[i][j] == 'X') or (board[i][j] == 'O'):
				counter = counter + 1
				if counter == max_counter:
					return 3

			if (board[i][j] == ' '):
				return 0


def clear_screen():
	import os
	os.system('cls' if os.name == 'nt' else 'clear')


def local_2_player_game():
	player = 1
	board = create_board()

	while True:
		print_board(board)
		print(f"Executing turn for player {player}")
		column_chosen = execute_player_turn(player, board)
		# print(f"Dropping for player {player}")
		# dropped = drop_piece(board,player, column_chosen)

		# print(f"Drop was {dropped}")
		if column_chosen is not None:
			if player == 1:
				player = 2
			else:
				player = 1
			
		end_of_game(board)

if __name__ == "__main__":
	local_2_player_game()