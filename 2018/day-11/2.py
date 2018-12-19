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

# return (x, y, power)
def search_best_for_size(serial, size, field):
    f = field
    w = WIDTH - size + 1
    h = HEIGHT - size + 1

    best = (0, 0, 0)
    for y in xrange(h):
        for x in xrange(w):
            p = 0
            for dy in xrange(size):
                p += sum(f[y + dy][x : x + size])
            if p > best[2]:
                best = (x + 1, y + 1, p)
    return best

# return (x, y, size, power)
def search_best_size(serial):
    f = fill_field(serial)
    best = search_best_for_size(serial, 1, f)
    best_size = 1
    for size in xrange(2, WIDTH + 1):
        best4size = search_best_for_size(serial, size, f)
        if best4size[2] > best[2]:
            best_size = size
            best = best4size

    return best[0], best[1], best_size, best[2]


# search_best test

# For grid serial number 18, the largest total square (with a total power of 113)
# is 16x16 and has a top-left corner of 90,269, so its identifier is 90,269,16.
#
# For grid serial number 42, the largest total square (with a total power of 119)
# is 12x12 and has a top-left corner of 232,251, so its identifier is 232,251,12.

# x, y, size, power = search_best_size(18)
# assert((x == 90) and (y == 269) and (size == 16) and (power == 113))

SERIAL = 6392
best = search_best_size(SERIAL)
print best
print 'Answer: %d,%d,%d' % (best[0], best[1], best[2])

# results
# Answer: 233,268,13
# real    3m57.631s (pypy)
