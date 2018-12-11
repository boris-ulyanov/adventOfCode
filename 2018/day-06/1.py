#!/usr/bin/python

import sys
from collections import defaultdict

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
if False:
    data_lines = [
        '1, 1\n',
        '1, 6\n',
        '8, 3\n',
        '3, 4\n',
        '5, 5\n',
        '8, 9\n'
    ]

data = [ tuple(map(int, line[:-1].split(', '))) for line in data_lines]
data_lines = None
data_len = len(data)

# bounds
min_x, max_x = data[0][0], data[0][0]
min_y, max_y = data[0][1], data[0][1]
for d in data:
    print d
    min_x = min(min_x, d[0])
    max_x = max(max_x, d[0])
    min_y = min(min_y, d[1])
    max_y = max(max_y, d[1])

print 'data size:', data_len
print 'range x', min_x, ':', max_x
print 'range y', min_y, ':', max_y

# create field
width = max_x - min_x + 1
height = max_y - min_y + 1
field = []
for y in xrange(height):
    field.append([-1] * width)

def mdistance(cell, x, y):
    return abs(cell[0] - x) + abs(cell[1] - y)

# scan over field
for y in xrange(height):
    for x in xrange(width):
        nearest = 0    # index nearest point or '.' if shared
        min_dist = mdistance(data[0], x + min_x, y + min_y)
        for idx in xrange(1, data_len):
            dist = mdistance(data[idx], x + min_x, y + min_y)
            if dist < min_dist:
                min_dist = dist
                nearest = idx
            elif dist == min_dist:
                nearest = -1

        field[y][x] = nearest

# areas size (-1 if unlimited)
areas = [0] * data_len

for row in field:
    for cell in row:
        if cell < 0:
            continue
        areas[cell] += 1

# exclude unlimited
for x in xrange(width):
     f = field[0][x]
     if f >= 0:
        areas[f] = -1
     f = field[height - 1][x]
     if f >= 0:
        areas[f] = -1

for y in xrange(height):
     f = field[y][0]
     if f >= 0:
        areas[f] = -1
     f = field[y][width - 1]
     if f >= 0:
        areas[f] = -1

print areas
max_area = max(areas)
print 'Answer', max_area

# results
# Answer 3696
