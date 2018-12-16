#!/usr/bin/python

import sys
from collections import defaultdict

# 427 players; last marble is worth 70723 points

PLAYERS_COUNT = 427
LAST_WORTH = 70723 * 100

# test
#
# PLAYERS_COUNT = 9
# LAST_WORTH = 25
#
#  9 players; last marble is worth   25 points: high score is 32
# 10 players; last marble is worth 1618 points: high score is 8317
# 13 players; last marble is worth 7999 points: high score is 146373
# 17 players; last marble is worth 1104 points: high score is 2764
# 21 players; last marble is worth 6111 points: high score is 54718
# 30 players; last marble is worth 5807 points: high score is 37305


cur = [0, 1, 2]
cur[1] = cur    # prev
cur[2] = cur    # next
zero = cur

points = defaultdict(int)

for x in xrange(1, LAST_WORTH + 1):

    if (x % 23) == 0:
        player = ((x - 1) % PLAYERS_COUNT) + 1
        points[player] += x
        for i in xrange(7):
            cur = cur[1]

        points[player] += cur[0]
        cur[1][2] = cur[2]  # prev to next
        cur[2][1] = cur[1]  # next to prev
        cur = cur[2]
        continue

    prev_item = cur[2]
    next_item = prev_item[2]

    cur = [x, prev_item, next_item]
    prev_item[2] = cur
    next_item[1] = cur


# cur = zero
# while True:
#     print cur[0],
#     cur = cur[2]
#     if cur == zero:
#         break


# print points
print 'Answer', max(points.values())

# results 5.5sec vs 270 mins
# Answer 3349098263
