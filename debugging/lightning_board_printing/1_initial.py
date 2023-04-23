def print_board(board):
    print("========== Connect4 =========")
    print("Player 1: X       Player 2: O\n")
    print("  1   2   3   4   5   6   7", end = '')

    for row in range(6):
        print("\n --- --- --- --- --- --- ---")
        print("|", end = " ")
        for col in range(7):
            if (board[row][col]) == 0:
                print(" ", end = " | ")
            elif (board[row][col]) == 1:
                print("X ", end = " | ")
            elif (board[row][col]) == 2:
                print("O ",end = " | ")

    print("\n --- --- --- --- --- --- ---")
    print("=============================")

def create_board():
    # Copy your solution from task 2 here
    board = []
    outer = range(6)
    for square in outer:
        row = []
        inner = range(7)
        for column in inner:
            row.append(0)
        board.append(row)
    return board

    # Enter test code below
if __name__ == "__main__":
    board = create_board()
    print_board(board)