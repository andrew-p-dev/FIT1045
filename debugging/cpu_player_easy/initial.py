import random

def drop_piece(board, player, column):
  row = 5
  count = 6
  check = False
  while count > 0:
    if board[row][column - 1] != 0:
      row -= 1
      count -= 1
    else:
      board[row][column - 1] += player
      check = True
      break
  return check

def create_board():
  board = [[0 for x in range(7)] for y in range(6)]
  return board


def cpu_player_easy(board, player):
  check = False
  while not check:
    column = int(random.uniform(0, 6))
    check = drop_piece(board, player, column)

if __name__ == "__main__":
  board = create_board()
  cpu_player_easy(board, 2)
  for row in board:
    print(row)