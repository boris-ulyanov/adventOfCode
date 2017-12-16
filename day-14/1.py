#!/usr/bin/python

puzzle_input = 'xlqgujun'
# puzzle_input = 'flqrgnkx'   # test

def knot_hach(data):
    rotations = [ord(sym) for sym in data] + [17, 31, 73, 47, 23]
    # print
    # print 'data:', data
    # print
    # print 'rotations:', rotations

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

    # print
    # print 'dense_hash', dense_hash
    # for i in xrange(16):
    #     print '%02x' % dense_hash[i],
    # print
    # print 'str form:', ''.join(["%02x" % n for n in dense_hash])

    return dense_hash

def bits_in_byte(h):
    #      0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
    h2b = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
    h1 = h >> 4
    h2 = h & 0xf
    return h2b[h1] + h2b[h2]

# test hash
# res = knot_hach("AoC 2017")
# for i in xrange(16):
#     print '%02x' % res[i],

used = 0

for row in xrange(128):
    hash_in = puzzle_input + '-' + str(row)
    hash_out = knot_hach(hash_in)
    # print hash_in, '=>',
    # for i in xrange(16):
    #     print '%02x' % hash_out[i],
    # print

    # test print
    # for col in xrange(8):
    #     b = col / 8
    #     shift = (7 - (col % 8))
    #     v = (hash_out[b] >> shift) & 0x01
    #     print '%d' % v,
    # print

    for b in hash_out:
        used += bits_in_byte(b)

print 'Used:', used
