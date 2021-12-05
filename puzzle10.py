"""
--- Day 5: Hydrothermal Venture ---
--- Part Two ---

Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

    An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
    An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....

You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?

-----
DATA DOWNLOADED FROM https://adventofcode.com/2021/day/5/input

"""

"""
"""


# small file
from pprint import pprint
input_filename = 'input_day05_small.txt'
# big file
# input_filename = 'input_day05.txt'


def check_dangerous_areas():
    """checks the grid for dangerous areas. A dangerous area
    is identified, when the crossing line index is 2 or greater.
    """
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
        print(output)

    # at the end, print the amount of dangerous areas
    print(f'Found {dangerous_areas} dangerous areas')

    # end od def ------------------------------------------


def create_grid(lines):
    """creates a grid based on the line inputs

    Args:
        lines (array): the parsed lines from the file

    Returns:
        [[array]array]: a 2d-array with the maximum size in col and row
    """
    max_x = 0
    max_y = 0

    for line in lines:
        p1, arrow, p2 = line.split()
        x1, y1 = [int(s) for s in p1.split(',')]
        x2, y2 = [int(s) for s in p2.split(',')]

        max_x = max(max(max_x, x1), max(max_x, x2))
        max_y = max(max(max_y, y1), max(max_y, y2))

    # increase max x and y by one for range function
    max_x += 1
    max_y += 1
    grid = [[0 for x in range(max_x)] for y in range(max_y)]
    print(f'created a grid with {max_x} * {max_y} fields')
    return grid

    # end of def ------------------------------------------


def process_grid(grid, lines):
    """processes the lines data on the grid and draws the
    horizontal, vertical and diagonal lines

    Args:
        grid ([array]array): the 2d array to work on
        lines (array): an array of strings read line by line from the input file
    """
    for line in lines:
        p1, arrow, p2 = line.split()
        x1, y1 = [int(s) for s in p1.split(',')]
        x2, y2 = [int(s) for s in p2.split(',')]

        # only if we have horizontal or vertical line, process it
        if x1 == x2:
            draw_horizontal_line(y1, y2, grid, x1)
        elif y1 == y2:
            draw_vertical_line(x1, x2, grid, y1)
        else:
            draw_diagonal_line(x1, y1, grid, x2, y2)


def draw_horizontal_line(y1, y2, grid, x):
    """draw a horizontal line on the grid from
    colunm y1 to y2 on height x

    Args:
        y1 (int): starting point on x axis
        y2 (int): ending point on x axis
        grid (array): the grid to work on
        x (int): the x axis (row) on which the line will be drawn
    """
    for y in range(min(y1, y2), max(y1, y2) + 1):
        grid[y][x] = grid[y][x] + 1


def draw_vertical_line(x1, x2, grid, y):
    """draw a vertical line on the grid from
    row x1 to x2 on column y

    Args:
        x1 (int): starting point on y axis
        x2 (int): ending point on y axis
        grid (array): the grid to work on
        y (int): the y axis (column) on which the column will be drawn
    """

    for x in range(min(x1, x2), max(x1, x2) + 1):
        grid[y][x] = grid[y][x] + 1


def draw_diagonal_line(x1, y1, grid, x2, y2):
    """draws a diagonal line on the grid from the
    starting point to the end point. As we only have
    45 degree diagonal lines, we can calculate the
    maximum steps and then determine the direction on the
    x and y axis (going left or right, up or down).
    Then start at the x1 and y1 for the calculted steps and
    move in the right directions

    Args:
        x1 (int): the starting point on x axis
        y1 (int): starting point on y axis
        grid ([array]array): the 2d grid array
        x2 (int): end point on x axis
        y2 (int): end point on y axis
    """
    # processing diagonal lines
    x = x1
    y = y1
    # how many steps
    steps = y1 - y2
    if steps < 0:
        steps = -steps
    # increase by one as the internal grid starts with 0
    steps += 1

    # go up or down
    if x2 < x1:
        step_x = -1
    else:
        step_x = 1

    # go up or down
    if y2 < y1:
        step_y = -1
    else:
        step_y = 1

    for i in range(steps):
        grid[y][x] += 1
        x += step_x
        y += step_y





# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # read in lines from intput
    file = open(input_filename, 'r')
    lines = file.read().splitlines()

    grid = create_grid(lines)
    process_grid(grid, lines)
    check_dangerous_areas()
