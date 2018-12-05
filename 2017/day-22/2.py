#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
# data_lines = [
#     '..#',
#     '#..',
#     '...',
# ]


###########
# methods
###########

def dump(img):
    for yy in xrange(len(img)):
        print
        for xx in xrange(len(img[yy])):
            print img[yy][xx],
    print '\n'

def set_patern(img, sx, sy, pattern):
    size = len(pattern)
    for yy in xrange(size):
        img[sy + yy][sx:sx + size] = pattern[yy]


###########
# parse input => make field
###########

if data_lines[0][-1] == '\n':
    for ii in xrange(len(data_lines)):
        data_lines[ii] = data_lines[ii][:-1]

SIZE = 1000
field = [['.' for i in xrange(SIZE)] for j in xrange(SIZE)]

sxy = (len(field) - len(data_lines)) / 2

set_patern(field, sxy, sxy, data_lines)


x = (len(field) - 1) / 2
y = x

direction = 0   # 0 - up; 1 - right; ...

counter = 0

for step in xrange(10000000):

    if (step % 10000) == 0:
        print step, x, y

    f = field[y][x]

    if f == '.':
        field[y][x] = 'W'
        direction += -1
    elif f == 'W':
        field[y][x] = '#'
        # direction += -1
        counter += 1
    elif f == '#':
        field[y][x] = 'F'
        direction += 1
    elif f == 'F':
        field[y][x] = '.'
        direction += 2
    else:
        print 'f:', f


    if direction < 0:
        direction += 4
    elif direction > 3:
        direction -= 4

    if direction == 0:
        y -= 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y += 1
    elif direction == 3:
        x += -1
    else:
        print 'Unexpected dir', direction

    if (x < 0) or (x >= SIZE) or (y < 0) or (y >= SIZE):
        print 'Outrange xy', x, y, step


# dump(field)

print 'infection', counter
