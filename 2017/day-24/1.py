#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
# data_lines = [
#     '0/2',
#     '2/2',
#     '2/3',
#     '3/4',
#     '3/5',
#     '0/1',
#     '10/1',
#     '9/10',
# ]

items = [ map(int, line.split('/')) for line in data_lines ]
data_lines = None

# level = 0

def max_tail(connector, used_list):
    # global level
    # pre = '   ' * level
    # level += 1
    # print pre, 'connector', connector

    used_copy = list(used_list)
    max_mass = 0
    max_idx = -1
    max_trace = []

    for idx in xrange(len(items)):
        # print pre, 'Check idx', idx,

        if used_copy[idx]:
            # print pre, 'used'
            continue

        item = items[idx]

        next_connector = None
        if item[0] == connector:
            next_connector = item[1]
        elif item[1] == connector:
            next_connector = item[0]
        else:
            # print pre, 'not fit'
            continue

        # print pre, '==> accepted'

        used_copy[idx] = True

        mass, trace = max_tail(next_connector, used_copy)
        mass += connector + next_connector

        # print pre, '==> mass', mass

        if max_mass < mass:
            max_mass = mass
            max_idx = idx
            max_trace = trace

        used_copy[idx] = False

    if max_mass > 0:
        max_trace = [max_idx] + max_trace

    # print pre, 'return mass', max_mass
    # level -= 1
    return max_mass, max_trace


nothing_used = [ False for x in xrange(len(items)) ]

mass, trace = max_tail(0, nothing_used)

print 'mass', mass
print 'trace', trace
for idx in trace:
    print '[%d/%d] ' % (items[idx][0], items[idx][1]),
