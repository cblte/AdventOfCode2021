"""
--- Day 5: Hydrothermal Venture ---

You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

    An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....

In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?


-----
DATA DOWNLOADED FROM https://adventofcode.com/2021/day/5/input

"""

"""
"""

from pprint import pprint


def print_grid_with_dots():
    dangerous_areas = 0

    for x in range(0, len(grid)):
        output = ''
        for y in range(0, len(grid[0])):
            if grid[x][y] == 0:
                output += '.'
            else:
                output += f'{grid[x][y]}'

            if grid[x][y] >= 2:
                dangerous_areas += 1
        # print(output)

    # at the end, print the amount of dangerous areas
    print(f'Found {dangerous_areas} dangerous areas')


def create_grid(lines):
    max_x = 0
    max_y = 0

    for line in lines:
        p1, arrow, p2 = line.split()
        x1, y1 = [int(s) for s in p1.split(',')]
        x2, y2 = [int(s) for s in p2.split(',')]

        max_x = max ( max(max_x, x1), max(max_x, x2) )
        max_y = max ( max(max_y, y1), max(max_y, y2) )

    # increase max x and y by one for range function
    max_x += 1
    max_y += 1
    grid = [[0 for x in range(max_x)] for y in range(max_y)]
    print(f'created a grid with {max_x} * {max_y} fields')
    return grid


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #file = open('input_day05_small.txt', 'r')
    file = open('input_day05.txt', 'r')
    lines = file.read().splitlines()

    grid = create_grid(lines)


    for line in lines:
        p1, arrow, p2 = line.split()
        x1, y1 = [int(s) for s in p1.split(',')]
        x2, y2 = [int(s) for s in p2.split(',')]
        print(x1, y1, x2, y2)

        # only if we have horizontal or vertical line, process it
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2) + 1):
                grid[y][x1] = grid[y][x1] + 1
        elif y1 == y2:
            for x in range(min(x1,x2), max(x1, x2) + 1):
                grid[y1][x] = grid[y1][x] + 1

    print_grid_with_dots()