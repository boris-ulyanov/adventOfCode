#!/usr/bin/python

import sys
from collections import defaultdict

WIDTH = 300
HEIGHT = 300

def power_level(serial, x, y):
    rack_id = x + 10
    power_level = rack_id * y
    xxx = (power_level + serial) * rack_id
    return ((xxx % 1000) / 100) - 5

def fill_field(serial):
    field = [[0] * WIDTH  for x in xrange(HEIGHT)]
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            field[y][x] = power_level(serial, x + 1, y + 1)
    return field

# return (power, x, y)
def search_best_for_size(serial, size, field):
    f = field
    w = WIDTH - size + 1
    h = HEIGHT - size + 1

    # p_by_rows = [0] * size
    best = (-5 * WIDTH * HEIGHT, 0, 0)
    for y in xrange(h):

        # fill first piece
        p = 0
        for dy in xrange(size):
            # p_by_rows[dy] = sum(f[y + dy][0 : size])
            p += sum(f[y + dy][0 : size])

        if p > best[0]:
            best = (p, 1, y + 1)

        for x in xrange(1, w):

            for dy in xrange(size):
                p -= f[y + dy][x-1]
                p += f[y + dy][x + size - 1]

            if p > best[0]:
                best = (p, x + 1, y + 1)
    return best


# For grid serial number 18, the largest total 3x3 square has a top-left corner of 33,45
# (with a total power of 29); these fuel cells appear in the middle of this 5x5 region:
f = fill_field(18)
best = search_best_for_size(18, 3, f)
assert((best[0] == 29) and (best[1] == 33) and (best[2] == 45))

# For grid serial number 42, the largest 3x3 square's top-left is 21,61
# (with a total power of 30); they are in the middle of this region:
f = fill_field(42)
best = search_best_for_size(42, 3, f)
assert((best[0] == 30) and (best[1] == 21) and (best[2] == 61))

# return (x, y, size, power)
def search_best_size(serial):
    f = fill_field(serial)
    best = search_best_for_size(serial, 1, f)
    best_size = 1
    # for size in xrange(2, 20):
    for size in xrange(2, WIDTH + 1):
        best4size = search_best_for_size(serial, size, f)
        if best4size[0] > best[0]:
            best_size = size
            best = best4size
    return best[0], best[1], best[2], best_size

# search_best_size test

# For grid serial number 18, the largest total square (with a total power of 113)
# is 16x16 and has a top-left corner of 90,269, so its identifier is 90,269,16.
#
# For grid serial number 42, the largest total square (with a total power of 119)
# is 12x12 and has a top-left corner of 232,251, so its identifier is 232,251,12.

x, y, size, power = search_best_size(18)
# assert((x == 90) and (y == 269) and (size == 16) and (power == 113))

# # For grid serial number 42, the largest 3x3 square's top-left is 21,61
# # (with a total power of 30); they are in the middle of this region:
# best = search_best(42)
# assert((best[0] == 21) and (best[1] == 61) and (best[2] == 30))

# SERIAL = 6392
# best = search_best(SERIAL)
# print best
# print 'Answer: %d,%d' % (best[0], best[1])

# results
# Answer 45865
