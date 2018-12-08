#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
# data_lines = ['#1 @ 1,3: 4x4\n', '#2 @ 3,1: 4x4\n', '#3 @ 5,5: 2x2\n']

print 'readed recs:', len(data_lines)

# def dump_field():
#     for y in xrange(max_y + 1):
#         print field[y]
#     print

# parse input line, return x1, y1, x2, y2
def parse_line(line):
    idx1 = line.find('@')
    idx2 = line.find(':')
    assert(idx1 > 0 and idx2 > 0)

    id = line[1:idx1]

    coords = line[idx1 + 2:idx2].split(',')
    x = int(coords[0])
    y = int(coords[1])

    size = line[idx2 + 2:-1].split('x')
    w = int(size[0])
    h = int(size[1])

    # print line, ' => ', x , y, w, h
    return (x, y, x + w - 1, y + h - 1, id)

boxes = map(parse_line, data_lines)
data_lines = None

# calc size
max_x = 0
max_y = 0
for b in boxes:
    if max_x < b[2]:
        max_x = b[2]
    if max_y < b[3]:
        max_y = b[3]

print 'maxes: ', max_x, max_y

# prepare field
field = []
for x in xrange(max_y + 1):
    field.append([0] * (max_x + 1))

# dump_field()

# fill field
for b in boxes:
    for y in xrange(b[1], b[3] + 1):
        dest_row = field[y]
        for x in xrange(b[0], b[2] + 1):
            dest_row[x] += 1

# dump_field()

# check which is not intersected
for b in boxes:
    intersected = False
    for y in xrange(b[1], b[3] + 1):
        dest_row = field[y]
        for x in xrange(b[0], b[2] + 1):
            if dest_row[x] > 1:
                intersected = True
    if not intersected:
        print 'not intersected', b[4]
