#!/usr/bin/python

import sys
from collections import defaultdict

# 427 players; last marble is worth 70723 points

PLAYERS_COUNT = 427
LAST_WORTH = 70723

# test
#
# PLAYERS_COUNT = 10
# LAST_WORTH = 1618
#
#  9 players; last marble is worth   25 points: high score is 32
# 10 players; last marble is worth 1618 points: high score is 8317
# 13 players; last marble is worth 7999 points: high score is 146373
# 17 players; last marble is worth 1104 points: high score is 2764
# 21 players; last marble is worth 6111 points: high score is 54718
# 30 players; last marble is worth 5807 points: high score is 37305

data = [0]
cur = 0
points = defaultdict(int)

for x in xrange(1, LAST_WORTH + 1):
    l = len(data)
    if (x % 23) == 0:
        player = ((x - 1) % PLAYERS_COUNT) + 1
        points[player] += x
        pos = cur - 7
        if pos < 0:
            pos += l
        points[player] += data[pos]
        data = data[:pos] + data[pos + 1:]
        cur = pos
        if cur == l:
            cur = 0
        continue

    pos = cur + 2
    if pos > l:
        pos -= l
    data.insert(pos, x)
    cur = pos

# print points
print 'Answer', max(points.values())

# results
# Answer 399745
