#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

particles = []


def parse_vec(in_str):
    return [int(sub_str) for sub_str in in_str.split(',')]


for line in data_lines:
    starts =  [pos for pos in xrange(len(line)) if line[pos] == '<']
    ends =  [pos for pos in xrange(len(line)) if line[pos] == '>']

    p = parse_vec(line[starts[0] + 1:ends[0]])
    v = parse_vec(line[starts[1] + 1:ends[1]])
    a = parse_vec(line[starts[2] + 1:ends[2]])
    particles.append([p, v , a])


min_value = 1000    # Fix it
min_index = -1

for i in xrange(len(particles)):
    p = particles[i]
    a = p[2]
    m = (a[0] * a[0]) + (a[1] * a[1]) + (a[2] * a[2])

    if m < min_value:
        min_value = m
        min_index = i

print 'min_index', min_index
print 'min_value', min_value
print 'particles', particles[min_index][2]
