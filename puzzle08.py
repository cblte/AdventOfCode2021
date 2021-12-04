"""
--- Day 4: Giant Squid ---
--- Part Two ---

On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?


-----
DATA DOWNLOADED FROM https://adventofcode.com/2021/day/4/input

"""

"""
Todo:
- when a board has a bing, remove it from the list of avaiable cards
- continue drawing numbers for the remaining cards until only one card is left
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
                    # print(f'Replacing {number} on card {i}-{row}/{col}')
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

            # save cards in second array so we can remove all
            # cards with bingo
            cards_to_check = bingo_cards
            for card in cards_to_check:
                if is_bingo(card):
                    card_index = bingo_cards.index(card)
                    bingo_cards.remove(card)
                    print(f'BINGO found on card {card_index} - removing it from the stack. {len(bingo_cards)} left to play with')


            # if no cards are left, the the last card we played
            # with is the one which will win last with the
            # last draw number.
            if len(bingo_cards) == 0:
                break


    # calc sum for the remaining card
    sum_of_all = sum_up_all_non_marked_numbers(card)
    print(f'Score to win against the squid: {number}*{sum_of_all}={int(number) * sum_of_all}')
