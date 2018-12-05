#!/usr/bin/python

puzzle_input = 'xlqgujun'
# puzzle_input = 'flqrgnkx'   # test

def knot_hach(data):
    rotations = [ord(sym) for sym in data] + [17, 31, 73, 47, 23]
    data_size = 256
    data = [x for x in xrange(data_size)]

    skip_size = 0
    cur_pos = 0

    for x in xrange(64):
        for rot in rotations:
            if rot > 1:
                end = cur_pos + rot
                if end > data_size:
                    # two piece
                    # [tail_size ... (x)==>]
                    tail_size = end - data_size
                    tmp = data[cur_pos:] + data[0:tail_size]
                    tmp = list(reversed(tmp))

                    data[cur_pos:] = tmp[0:-tail_size]
                    data[0:tail_size] = tmp[-tail_size:]
                else:
                    # one piece
                    tmp = data[cur_pos:end]
                    tmp = list(reversed(tmp))
                    data[cur_pos:end] = tmp

            else:
                pass
                # print '> no action'

            cur_pos = (cur_pos + rot + skip_size) % data_size
            skip_size += 1

    dense_hash = [0 for x in xrange(16)]

    for i in xrange(16):
        start = i * 16
        value = 0
        for j in xrange(16):
            value = value ^ data[start + j]
        dense_hash[i] = value

    return dense_hash


field = [[False for x in xrange(128)] for y in xrange(128)]


for row in xrange(128):
    hash_in = puzzle_input + '-' + str(row)
    hash_out = knot_hach(hash_in)

    for col in xrange(128):
        b = col / 8
        shift = (7 - (col % 8))
        v = (hash_out[b] >> shift) & 0x01
        field[row][col] = '#' if v != 0 else '.'


# search all regions
def fill_region(reg_num, row, col):
    field[row][col] = reg_num
    if ((row > 0) and (field[row - 1][col] == '#')):
        fill_region(reg_num, row - 1, col)
    if ((row < 127) and (field[row + 1][col] == '#')):
        fill_region(reg_num, row + 1, col)
    if ((col > 0) and (field[row][col - 1] == '#')):
        fill_region(reg_num, row, col - 1)
    if ((col < 127) and (field[row][col + 1] == '#')):
        fill_region(reg_num, row, col + 1)


regions = 0
for row in xrange(128):
    for col in xrange(128):
        if field[row][col] == '#':
            regions += 1
            fill_region(regions, row, col)

print 'Regions', regions

# output field
# for row in xrange(8):
#     print
#     for col in xrange(8):
#         v = field[row][col]
#         v = '.' if v == False else str(v)
#         print v,
