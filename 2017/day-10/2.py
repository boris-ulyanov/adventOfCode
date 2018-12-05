#!/usr/bin/python

data = "157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30"
# data = "AoC 2017"

rotations = [ord(sym) for sym in data] + [17, 31, 73, 47, 23]

print
print 'data:', data
print
print 'rotations:', rotations



data_size = 256
# data_size = 5   # 0 1 2 3 4

data = [x for x in xrange(data_size)]

skip_size = 0
cur_pos = 0

for x in xrange(64):
    for rot in rotations:
        # print
        # print 'rot', rot
        # print 'cur_pos', cur_pos
        # print 'skip_size', skip_size
        # print 'pre:', data

        if rot > 1:

            end = cur_pos + rot

            if end > data_size:
                # two piece
                # [tail_size ... (x)==>]
                tail_size = end - data_size
                # print 'two piece tail_size', tail_size

                tmp = data[cur_pos:] + data[0:tail_size]
                # print 'tmp pre', tmp
                tmp = list(reversed(tmp))
                # print 'tmp after', tmp

                data[cur_pos:] = tmp[0:-tail_size]
                data[0:tail_size] = tmp[-tail_size:]

            else:
                # one piece
                # print 'one piece'
                tmp = data[cur_pos:end]
                # print 'tmp pre', tmp
                tmp = list(reversed(tmp))
                # print 'tmp after', tmp
                data[cur_pos:end] = tmp

        else:
            pass
            # print '> no action'

        # print 'after:', data

        cur_pos = (cur_pos + rot + skip_size) % data_size
        skip_size += 1

# print
# print 'data:', data


dense_hash = [0 for x in xrange(16)]

for i in xrange(16):
    start = i * 16
    value = 0
    for j in xrange(16):
        value = value ^ data[start + j]
    dense_hash[i] = value

print
print 'dense_hash', dense_hash
for i in xrange(16):
    print '%02x' % dense_hash[i],


print
print 'str form:', ''.join(["%02x" % n for n in dense_hash])




# print
# print 'cur_pos', cur_pos
# print 'skip_size', skip_size
# print data[0] * data[1]
