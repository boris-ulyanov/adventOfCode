#!/usr/bin/python

import sys

tgt_num = 368078
# tgt_num = 30

field_size = 11

gField = [[0 for j in xrange(field_size)] for i in xrange(field_size)]


def my_dump(field):
    print '--'
    for row in field:
        for e in row:
            print '%06d' % e,
        print

def calc_neighbors(field, x, y):
    r = 0
    r += field[y - 1][x - 1] + field[y - 0][x - 1] + field[y + 1][x - 1]
    r += field[y - 1][x - 0] +                       field[y + 1][x - 0]
    r += field[y - 1][x + 1] + field[y - 0][x + 1] + field[y + 1][x + 1]
    field[y][x] = r
    if r > tgt_num:
        print 'r:', r, 'x/y:', x, y
        my_dump(field)
        sys.exit()


x = (field_size - 1) / 2
y = (field_size - 1) / 2

gField[y][x] = 1

side_size = 0

while True:

    x += 1
    y += 1
    side_size += 2

    # to up
    for i in xrange(side_size):
        y -= 1
        calc_neighbors(gField, x, y)

    # to left
    for i in xrange(side_size):
        x -= 1
        calc_neighbors(gField, x, y)

    # to down
    for i in xrange(side_size):
        y += 1
        calc_neighbors(gField, x, y)

    # to right
    for i in xrange(side_size):
        x += 1
        calc_neighbors(gField, x, y)

print 'fail'

my_dump(gField)

