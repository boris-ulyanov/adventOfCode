#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

steps = data_lines[0].split(',')
data_lines = None

def calc_away(x, y):
    x = abs(x)
    y = abs(y)
    if x >= y:
        return x
    return x + (y - x) / 2

shifts = {
    'n': [0, 2],
    'nw': [-1, 1],
    'ne': [1, 1],
    's': [0, -2],
    'sw': [-1, -1],
    'se': [1, -1],
}

pos_x = 0
pos_y = 0

for step in steps:
    if step not in shifts:
        print 'not found: [%s]' % (step)

    shift = shifts[step]
    pos_x += shift[0]
    pos_y += shift[1]

print '-------'
print 'end position:', pos_x, pos_y
print
print 'end position distance:', calc_away(pos_x, pos_y)
