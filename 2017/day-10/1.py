#!/usr/bin/python

rotations = [157, 222, 1, 2, 177, 254, 0, 228, 159, 140, 249, 187, 255, 51, 76, 30]
# rotations = [3, 4, 1, 5]

data_size = 256
# data_size = 5   # 0 1 2 3 4

data = [x for x in xrange(data_size)]

skip_size = 0
cur_pos = 0

for rot in rotations:
    print
    print 'rot', rot
    print 'cur_pos', cur_pos
    print 'skip_size', skip_size
    # print 'pre:', data

    if rot > 1:

        end = cur_pos + rot

        if end > data_size:
            # two piece
            # [tail_size ... (x)==>]
            tail_size = end - data_size
            print 'two piece tail_size', tail_size

            tmp = data[cur_pos:] + data[0:tail_size]
            # print 'tmp pre', tmp
            tmp = list(reversed(tmp))
            # print 'tmp after', tmp

            data[cur_pos:] = tmp[0:-tail_size]
            data[0:tail_size] = tmp[-tail_size:]

        else:
            # one piece
            print 'one piece'
            tmp = data[cur_pos:end]
            # print 'tmp pre', tmp
            tmp = list(reversed(tmp))
            # print 'tmp after', tmp
            data[cur_pos:end] = tmp

    else:
        print '> no action'

    # print 'after:', data

    cur_pos = (cur_pos + rot + skip_size) % data_size
    skip_size += 1

print
print 'cur_pos', cur_pos
print 'skip_size', skip_size
print 'Answer:', data[0] * data[1]
