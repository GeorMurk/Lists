#!/usr/bin/python

#!2D Lists and Nested for Loops

#!2D List
grid_number = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
    [0]
]

print(grid_number[1][2])

#!Nested for_loop

for row in grid_number:
    print(row)

for row in grid_number:
    for col in row:
        print(col)

#!Go ahead and test it Out!!!!
