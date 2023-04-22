from dataclasses import dataclass
from os import system, name
from typing import Callable

RED = '🔴'
BLUE = '🔵'
BLANK = '\u3000'
K = 4
ROWS = 6
COLUMNS = 7
board = [[BLANK] * COLUMNS for _ in range(ROWS)]
height = [0 for _ in range(COLUMNS)]

def render():
  system('cls' if name == 'nt' else 'clear') # clear the shell
  print("".join([' ' + str(i) + ' ' for i in range(1, COLUMNS + 1)])) # print col number
  for row in board: # print the board
    print("".join([row[i] + '|' for i in range(COLUMNS)]))

render()

winner = None
player = BLUE
fullColumns = 0
while (winner is None):
  column = input('Drop piece: ')

  # Validation
  if not column.isdigit():
    print(f'Must be an int')
    continue

  column = int(str(column)) - 1
  if not 0 <= column <= COLUMNS - 1:
    print(f'Must be an int between 1 and {COLUMNS}')
    continue

  if height[column] == ROWS:
    print(f'Column {column + 1} is full')
    continue

  # update board
  height[column] += 1
  row = ROWS - height[column]
  board[row][column] = player
  render()

  # win/loss logic
  directions = [
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
  ]
  
  for direction in directions:
    count = 0
    x = column
    y = row
    while 0 <= x < COLUMNS and 0 <= y < ROWS and board[y][x] == player:
      count += 1
      if count == K:
        winner = player
        print("The winner is: " + winner)
        break
      x += direction[0]
      y += direction[1]

  if height[column] == ROWS:
    fullColumns += 1
    if fullColumns == COLUMNS:
      print("All columns full, no winner")
      break

  player = RED if player == BLUE else BLUE
  

  