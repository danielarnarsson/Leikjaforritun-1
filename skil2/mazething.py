import pygame
import random

#2 is where the player spawns in grid

grid =\
[
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
[1,2,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1]
[1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1]
[1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1]
[1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1]
[1,0,0,1,0,1,1,0,1,1,1,0,1,0,0,1,1,0,0,0,0,1]
[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]
[1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]
[1,0,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,1]
[1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1]
[1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1]
[1,0,0,0,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,0,0,1]
[1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1]
[1,0,0,0,0,0,1,0,1,0,1,1,1,1,0,0,0,0,0,0,0,1]
[1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1]
[1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1]
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1]
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
for y in range(1, 10,2):
    for x in range(1, 10, 2):
        grid[y][x] = 2

print(grid)