"""
--- Day 4: Giant Squid ---

You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?


-----
DATA DOWNLOADED FROM https://adventofcode.com/2021/day/4/input

"""

from pprint import pprint

# some global variables
bingo_numbers = []
bingo_cards = []


def get_column(list, i):
    return [row[i] for row in list]


def is_bingo(card):
    # checking rows
    for i in range(len(card)):
        row = card[i]
        number_of_x_in_row = [number for number in row if number == 'x']
        if len(number_of_x_in_row) == len(row):
            return True

    # checking columns
    for i in range(len(card)):
        column = get_column(card, i) # returns an array
        number_of_x_in_col = [number for number in column if number == 'x']
        if len(number_of_x_in_col) == len(column):
            return True

    # no bingo found
    return False


def check_cards_for_number(number):
    print(f'----------- CHECKING FOR NUMBER {number}')
    for i in range(0, len(bingo_cards)):
        card = bingo_cards[i]

        # look
        for row in range(len(card)):
            for col in range(len(card[row])):
                if card[row][col] == number:
                    print(f'Replacing {number} on card {i}-{row}/{col}')
                    card[row][col] = 'x'

        # saving back the card
        bingo_cards[i] = card


def sum_up_all_non_marked_numbers(card):
    print(f'Calculating sum for non marked numbers')
    sum = 0
    for row in card:
        for col in row:
            if col.isdigit():
                sum += int(col)
    return sum

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # file = open('input_day04_small.txt', 'r')
    file = open('input_day04.txt', 'r')
    lines = file.read().splitlines()

    # extracting the bingo numbers
    bingo_numbers = lines[0].split(',')

    # extracting bingo cards in steps of 5
    for i in range(2, len(lines), 6):
        card1 = lines[i].split()
        card2 = lines[i+1].split()
        card3 = lines[i+2].split()
        card4 = lines[i+3].split()
        card5 = lines[i+4].split()

        card = [card1, card2, card3, card4, card5]
        # append the card to the
        bingo_cards.append(card)

    print("---------- Looking for BINGO")
    bingo_found = False

    for number in bingo_numbers:
        # replace number on cards with 0 if match
        check_cards_for_number(number)

        # if more than 5 numbers are drawn, check cards for bingo
        if bingo_numbers.index(number) >= 5:
            for card in bingo_cards:
                if is_bingo(card):
                    print(f'BINGO found on card {bingo_cards.index(card)}')
                    pprint(card)
                    bingo_found = True
                    break

        # if a bingo was found, calulate result and quit the for loop
        if bingo_found:
            sum_of_all = sum_up_all_non_marked_numbers(card)

            print(f'Score to win against the squid: {number}*{sum_of_all}={int(number) * sum_of_all}')
            break
