#!/usr/bin/python

import math

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
# data_lines = [
    # 'p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>',
    # 'p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>',
    # 'p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>',
    # 'p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>',

    # 'p=< 8,9,10>, v=<1,0,0>, a=< 0,0,0>',
    # 'p=< 8,9,10>, v=<1,0,0>, a=< 0,0,0>',

    # 'p=< 0,9,10>, v=<1,0,0>, a=< 1,0,0>',
    # 'p=< -3,9,10>, v=<1,0,0>, a=< 2,0,0>',
# ]

particles = []


def parse_vec(in_str):
    return [int(sub_str) for sub_str in in_str.split(',')]

# parsing
for line in data_lines:
    starts =  [pos for pos in xrange(len(line)) if line[pos] == '<']
    ends =  [pos for pos in xrange(len(line)) if line[pos] == '>']

    p = parse_vec(line[starts[0] + 1:ends[0]])
    v = parse_vec(line[starts[1] + 1:ends[1]])
    a = parse_vec(line[starts[2] + 1:ends[2]])
    particles.append([p, v, a])


# return t or -1 if no coolide
def intersect(p1, p2, t):
    if t < 0:
        return -1
    for c in xrange(3):
        s1 = p1[0][c] + p1[1][c] * t + p1[2][c] * (t * t + t) / 2
        s2 = p2[0][c] + p2[1][c] * t + p2[2][c] * (t * t + t) / 2
        if (s1 - s2) != 0:
            return -1
    return t


# return t or -1 if no coolide
def check_collide(p1, p2):
    # for each axes
    for c in xrange(3):
        dp = p1[0][c] - p2[0][c]
        dv = p1[1][c] - p2[1][c]
        da = p1[2][c] - p2[2][c]

        # special cases
        if da == 0:
            if dv == 0:
                if dp == 0:
                    continue    # check other axes
                else:
                    return -1
            else:
                t = -dp / dv
                return intersect(p1, p2, t)

        # non standart accelerated move
        # square root S = S0 + V0*t + a*(t*t + t) / 2
        b = 2 * dv + da
        D = (b * b) - (4 * da * 2 * dp)
        if D < 0:
            return -1
        elif D == 0:
            t = -b / (2 * da)
            return intersect(p1, p2, t)
        else:
            D = math.sqrt(D)
            t = (-b + D) / (2 * da)
            rv = intersect(p1, p2, t)
            if rv >= 0:
                return rv
            t = (-b - D) / (2 * da)
            return intersect(p1, p2, t)

    return 0

# check collide
particles_len = len(particles)

# t, i1, i2
collides = []
col_indexes = set()

for i1 in xrange(particles_len):
    p1 = particles[i1]
    for i2 in xrange(i1 + 1, particles_len):
        p2 = particles[i2]
        t = check_collide(p1, p2)
        if t >= 0:
            # print 'Collide t:%f; i1:%d; i2:%d' %  (t, i1, i2)
            # print '\t-:', p1
            # print '\t-:', p2
            collides.append([t, i1, i2])
            col_indexes.update([i1, i2])

print 'particles_len', particles_len
print 'collides len', len(collides)

# print 'X', len(col_indexes), col_indexes

# answer (without checking twice colided particles)
print 'Answer', particles_len - len(col_indexes)
