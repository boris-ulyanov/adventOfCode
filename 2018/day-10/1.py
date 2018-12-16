#!/usr/bin/python

import sys
from collections import defaultdict

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
if False:
    data_lines = [
        'position=< 9,  1> velocity=< 0,  2>\n',
        'position=< 7,  0> velocity=<-1,  0>\n',
        'position=< 3, -2> velocity=<-1,  1>\n',
        'position=< 6, 10> velocity=<-2, -1>\n',
        'position=< 2, -4> velocity=< 2,  2>\n',
        'position=<-6, 10> velocity=< 2, -2>\n',
        'position=< 1,  8> velocity=< 1, -1>\n',
        'position=< 1,  7> velocity=< 1,  0>\n',
        'position=<-3, 11> velocity=< 1, -2>\n',
        'position=< 7,  6> velocity=<-1, -1>\n',
        'position=<-2,  3> velocity=< 1,  0>\n',
        'position=<-4,  3> velocity=< 2,  0>\n',
        'position=<10, -3> velocity=<-1,  1>\n',
        'position=< 5, 11> velocity=< 1, -2>\n',
        'position=< 4,  7> velocity=< 0, -1>\n',
        'position=< 8, -2> velocity=< 0,  1>\n',
        'position=<15,  0> velocity=<-2,  0>\n',
        'position=< 1,  6> velocity=< 1,  0>\n',
        'position=< 8,  9> velocity=< 0, -1>\n',
        'position=< 3,  3> velocity=<-1,  1>\n',
        'position=< 0,  5> velocity=< 0, -1>\n',
        'position=<-2,  2> velocity=< 2,  0>\n',
        'position=< 5, -2> velocity=< 1,  2>\n',
        'position=< 1,  4> velocity=< 2,  1>\n',
        'position=<-2,  7> velocity=< 2, -2>\n',
        'position=< 3,  6> velocity=<-1, -1>\n',
        'position=< 5,  0> velocity=< 1,  0>\n',
        'position=<-6,  0> velocity=< 2,  0>\n',
        'position=< 5,  9> velocity=< 1, -2>\n',
        'position=<14,  7> velocity=<-2,  0>\n',
        'position=<-3,  6> velocity=< 2, -1>\n'
    ]

# parsing
data = []
for line in data_lines:
    l = line[10:-2].split('=<')

    l1 = l[0].split()
    sx = int(l1[0][:-1])
    sy = int(l1[1][:-1])

    l1 = l[1].split(', ')
    vx = int(l1[0])
    vy = int(l1[1])

    data.append((sx, sy, vx, vy))

data_lines = None
data_len = len(data)


def makeStep(data, t):
    for i in xrange(data_len):
        d = data[i]
        data[i] = (d[0] + (t * d[2]), d[1] + (t * d[3]), d[2], d[3])

def getBounds(data):
    min_x = max_x = data[0][0]
    min_y = max_y = data[0][1]

    for i in xrange(1, data_len):
        d = data[i]
        min_x = min(min_x, d[0])
        max_x = max(max_x, d[0])
        min_y = min(min_y, d[1])
        max_y = max(max_y, d[1])

    w = max_x - min_x + 1
    h = max_y - min_y + 1
    return (w, h), (min_x, min_y, max_x, max_y)

def printState(data):
    # bounds
    size, bounds = getBounds(data)
    w = size[0]
    h = size[1]
    min_x, min_y = bounds[0], bounds[1]
    max_x, max_y = bounds[2], bounds[3]

    # fill field
    # field = bytearray()
    field = [False] * (w * h)

    for d in data:
        idx = (w * (d[1] - min_y)) + (d[0] - min_x)
        field[idx] = True

    for y in xrange(h):
        for x in xrange(w):
            idx = w * y + x

            if field[idx]:
                print 'X',
            else:
                print '.',
        print
    print


# find step with smallest size
data_copy = data[:]

smallest_size, _ = getBounds(data_copy)
smallest_step = 0
for x in xrange(1, 100000):
    makeStep(data_copy, 1)
    size, _ = getBounds(data_copy)
    if (size[0] + size[1]) > (smallest_size[0] + smallest_size[1]):
        break
    smallest_size = size
    smallest_step = x

print 'smallest_step', smallest_step

makeStep(data, smallest_step)
printState(data)

# results
# Answer JLPZFJRH
# Answer 10595
