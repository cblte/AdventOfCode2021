"""
--- Part Two ---
Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

199  A
200  A B
208  A B C
210    B C D
200  E   C D
207  E F   D
240  E F G
269    F G H
260      G H
263        H

Start by comparing the first and second three-measurement windows.
The measurements in the first window are marked
A (199, 200, 208); their sum is 199 + 200 + 208 = 607.
The second window is marked B (200, 208, 210); its sum is 618.
The sum of measurements in the second window is larger
than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of
measurements in this sliding window increases from the
previous sum. So, compare A with B, then compare B with C,
then C with D, and so on. Stop when there aren't enough
measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement
window is as follows:

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many
sums are larger than the previous sum?

-----
INPUT DOWNLOADED FROM https://adventofcode.com/2021/day/1/input
"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open('input_day01.txt', 'r')
    lines = file.read().splitlines()
    # creating a sums array which we fill with the sums of three values
    sums = []

    # print(lines)
    for i in range(0, len(lines)):
        # quit when we cannot sum three values
        if i + 2 >= len(lines):
            print('No more sums possible')
            break

        sum_of_three = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        sums.append(sum_of_three)
    print(f'Summed up the values. Found {len(sums)} three-measurement windows')

    # compare now the three measurement sums
    three_measurement_changed = 0
    print(f'{sums[0]} (N/A - no previous sum)')

    for i in range(1, len(sums)):
        if int(sums[i]) > int(sums[i - 1]):
            print(f'{sums[i]} (increased)')
            three_measurement_changed += 1
        elif int(sums[i]) == int(sums[i-1]):
            print(f'{sums[i]} (no change)')
        else:
            print(f'{sums[i]} (decreased)')

    print(f'In the current data set we have {three_measurement_changed} '
          f'sums that are larger than the previous sum.')

