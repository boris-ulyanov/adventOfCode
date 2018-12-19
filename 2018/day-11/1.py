#!/usr/bin/python

import sys
from collections import defaultdict

WIDTH = 300
HEIGHT = 300
STROB_WIDTH = 3
STROB_HEIGHT = 3

def power_level(serial, x, y):
    rack_id = x + 10
    power_level = rack_id * y
    xxx = (power_level + serial) * rack_id
    return ((xxx % 1000) / 100) - 5

# power_level test
t1 = power_level(8, 3, 5)
assert(t1 == 4)

def fill_field(serial):
    field = [[0] * WIDTH  for x in xrange(HEIGHT)]
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            field[y][x] = power_level(serial, x + 1, y + 1)
    return field


# fill_field test
# Fuel cell at  122,79, grid serial number 57: power level -5.
# Fuel cell at 217,196, grid serial number 39: power level  0.
# Fuel cell at 101,153, grid serial number 71: power level  4.
f = fill_field(57)
assert(f[79 - 1][122 - 1] == -5)

f = fill_field(39)
assert(f[196 - 1][217 - 1] == 0)

f = fill_field(71)
assert(f[153 - 1][101 - 1] == 4)


def search_best(serial):
    f = fill_field(serial)

    w = WIDTH - STROB_WIDTH + 1
    h = HEIGHT - STROB_HEIGHT + 1

    # power = [[0] * w for x in xrange(h)]
    best = (0, 0, 0)
    for y in xrange(h):
        for x in xrange(w):
            p = 0
            for dy in xrange(STROB_HEIGHT):
                p += sum(f[y + dy][x : x + STROB_WIDTH])

            if p > best[2]:
                best = (x + 1, y + 1, p)

    return best

# search_best test

# For grid serial number 18, the largest total 3x3 square has a top-left corner of 33,45
# (with a total power of 29); these fuel cells appear in the middle of this 5x5 region:
best = search_best(18)
assert((best[0] == 33) and (best[1] == 45) and (best[2] == 29))

# For grid serial number 42, the largest 3x3 square's top-left is 21,61
# (with a total power of 30); they are in the middle of this region:
best = search_best(42)
assert((best[0] == 21) and (best[1] == 61) and (best[2] == 30))

SERIAL = 6392
best = search_best(SERIAL)
print best
print 'Answer: %d,%d' % (best[0], best[1])

# results
# Answer 45865
