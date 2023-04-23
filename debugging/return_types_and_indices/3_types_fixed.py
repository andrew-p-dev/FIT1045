import random

def drop_piece(board: list[list[int]], player: int, column: int) -> bool:
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

def create_board() -> list[list[int]]:
  board = [[0 for x in range(7)] for y in range(6)]
  return board

def cpu_player_easy(board: list[list[int]], player: int) -> int:
  while True:
    column = int(random.uniform(0, 6))
    if drop_piece(board, player, column):
      return column

if __name__ == "__main__":
  print("Test with empty board:")
  board = create_board()
  for row in board:
    print(row)
  cpu_player_easy(board, 2)
  print("Result is:")
  for row in board:
    print(row)

  print()
  print("Test with only one free column:")
  board = board = [[1 for x in range(7)] for y in range(6)]
  for row in board[:3]:
    row[5] = 0
  for row in board:
    print(row)
  cpu_player_easy(board, 2)
  print("Result is:")
  for row in board:
    print(row)