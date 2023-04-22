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

@dataclass
class CheckDirection:
  startX: int
  startY: int
  incX: int
  incY: int
  next: Callable[[tuple[int, int]], tuple[int, int]]

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
  board[ROWS - height[column]][column] = player
  render()

  # win/loss logic
  directions = [
    CheckDirection(0, ROWS - 1, 1, 1, lambda x, y: (x, y - 1) if y > 0 else (x + 1, y)),
    CheckDirection(0, 0, -1, 1, lambda x, y: (x + 1, y) if x < COLUMNS - 1 else (x, y + 1)),
    CheckDirection(0, 0, 0, 1, lambda x, y: (x + 1, y)),
    CheckDirection(0, 0, 1, 0, lambda x, y: (x, y + 1)),
  ]
  
  for direction in directions:
    current = (direction.startX, direction.startY)

    while (winner is None and 0 <= current[0] < COLUMNS and 0 <= current[1] < ROWS):
      count = 0
      x = current[0]
      y = current[1]
      color = BLANK
      while 0 <= x < COLUMNS and 0 <= y < ROWS:
        if board[y][x] == color:
          count += 1
          if count == K and color != BLANK:
            winner = color
            print("The winner is: " + winner)
            break
        else:
          count = 1
          color = board[y][x]
        x += direction.incX
        y += direction.incY
        
      current = direction.next(current[0], current[1])

  if height[column] == ROWS:
    fullColumns += 1
    if fullColumns == COLUMNS:
      print("All columns full, no winner")
      break

  player = RED if player == BLUE else BLUE
  

  