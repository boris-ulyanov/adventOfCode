#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
# data_lines = [
#     '../.# => ##./#../...',
#     '.#./..#/### => #..#/..../..../#..#',
# ]


###########
# methods
###########

def sym_to_01(img):
    # (.#) => (01)
    for idx in xrange(len(img)):
        line = img[idx]
        img[idx] = [1 if sym == '#' else 0 for sym in line]

def flip(img):
    size = len(img)
    new_image = [[0 for i in xrange(size)] for i in xrange(size)]
    for yy in xrange(size):
        for xx in xrange(size):
            new_image[yy][xx] = img[size - yy - 1][xx]
    return new_image

def rotate(img):
    size = len(img)
    new_image = [[0 for i in xrange(size)] for i in xrange(size)]
    for yy in xrange(size):
        for xx in xrange(size):
            new_image[xx][size - yy - 1] = img[yy][xx]
    return new_image

def get_code(img, x, y, step):
    code = 0
    for yy in xrange(y, y + step):
        for xx in xrange(x, x + step):
            code = (code << 1) | img[yy][xx]
    return code | (step << 16)

def dump(img):
    size = len(img)
    for yy in xrange(size):
        print
        for xx in xrange(size):
            print img[yy][xx],
    print '\n'

def set_patern(img, sx, sy, pattern):
    # print 'set_patern', sx, sy,
    # print 'image:'
    # dump(img)
    # print 'pattern:'
    # dump(pattern)

    size = len(pattern)
    for yy in xrange(size):
        # print yy, sx, size
        img[sy + yy][sx:sx + size] = pattern[yy]


###########
# parse input => create rules cache
###########
rules = {}
for line in data_lines:
    lr = line.split(' => ')
    in_pattern = lr[0].split('/')
    out_pattern = lr[1].split('/')
    # print 'rule:'
    # print in_pattern, out_pattern
    sym_to_01(in_pattern)
    sym_to_01(out_pattern)

    # all in pattern variations - 4x rotate + flip + 4x rotate
    size = len(in_pattern)
    rules[get_code(in_pattern, 0, 0, size)] = out_pattern
    in_pattern = rotate(in_pattern)
    rules[get_code(in_pattern, 0, 0, size)] = out_pattern
    in_pattern = rotate(in_pattern)
    rules[get_code(in_pattern, 0, 0, size)] = out_pattern
    in_pattern = rotate(in_pattern)
    rules[get_code(in_pattern, 0, 0, size)] = out_pattern
    in_pattern = flip(in_pattern)
    rules[get_code(in_pattern, 0, 0, size)] = out_pattern
    in_pattern = rotate(in_pattern)
    rules[get_code(in_pattern, 0, 0, size)] = out_pattern
    in_pattern = rotate(in_pattern)
    rules[get_code(in_pattern, 0, 0, size)] = out_pattern
    in_pattern = rotate(in_pattern)
    rules[get_code(in_pattern, 0, 0, size)] = out_pattern


# for key in rules:
#     print '0x%x:' % key
#     print rules[key]

###########
# Initial image
###########
image = [
    '.#.',
    '..#',
    '###',
]

sym_to_01(image)

for iteration in xrange(18):

    image_size = len(image)
    two2three = image_size % 2 == 0
    step = 2 if two2three else 3
    step_new = 3 if two2three else 4
    blocks = image_size / step
    size_new = blocks * step_new
    image_new = [[0 for i in xrange(size_new)] for i in xrange(size_new)]

    for block_y in xrange(blocks):
        y = block_y * step
        y_new = block_y * step_new
        for block_x in xrange(blocks):
            x = block_x * step
            x_new = block_x * step_new
            code = get_code(image, x, y, step)
            set_patern(image_new, x_new, y_new, rules[code])

    print 'iteration', iteration + 1
    # print 'in image:'
    # dump(image)
    # print '==>> out image:'
    # dump(image_new)

    image = image_new

# count enabled pixels
pix_on_ctr = 0
for line in image:
    for pixel in line:
        pix_on_ctr += pixel

print 'Enabled pixels:', pix_on_ctr
