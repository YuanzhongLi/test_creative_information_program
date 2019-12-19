import sys
from Test import solve4

file_path = 'test001.txt'

maze = solve4(file_path)

for maze_row in maze:
  txt = ''
  for maze_mark in maze_row:
    txt += maze_mark
  print(txt)
