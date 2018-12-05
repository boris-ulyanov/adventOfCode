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

def sym_to_01(img):
    # (.#) => (01)
    for idx in xrange(len(img)):
        line = img[idx]
        img[idx] = [1 if sym == '#' else 0 for sym in line]

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

SIZE = 471
field = [[0 for i in xrange(SIZE)] for j in xrange(SIZE)]

sxy = (len(field) - len(data_lines)) / 2

sym_to_01(data_lines)
set_patern(field, sxy, sxy, data_lines)


x = (len(field) - 1) / 2
y = x

direction = 0   # 0 - up; 1 - right; ...

counter = 0

for step in xrange(10000):

    if field[y][x] == 1:
        field[y][x] = 0
        direction += 1
    else:
        field[y][x] = 1
        direction += -1
        counter += 1

    if direction < 0:
        direction = 3
    elif direction > 3:
        direction = 0

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


dump(field)

print 'infection', counter
