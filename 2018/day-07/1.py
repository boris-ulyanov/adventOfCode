#!/usr/bin/python

import sys
from collections import defaultdict

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
if False:
    data_lines = [
        'Step C must be finished before step A can begin.\n',
        'Step C must be finished before step F can begin.\n',
        'Step A must be finished before step B can begin.\n',
        'Step A must be finished before step D can begin.\n',
        'Step B must be finished before step E can begin.\n',
        'Step D must be finished before step E can begin.\n',
        'Step F must be finished before step E can begin.\n'
    ]

data = [ tuple([line[5:6], line[36:37]]) for line in data_lines]
data_lines = None
data_len = len(data)

# make dependency
dependency = defaultdict(list)
for d in data:
    dependency[d[1]].append(d[0])
    dependency[d[0]]

result = []

for _ in xrange(len(dependency)):
    ready = []
    for k, v in dependency.items():
        if len(v) == 0:
            ready.append(k)

    ready.sort()
    selected = ready[0]
    print 'selected', selected
    result.append(selected)

    del dependency[selected]

    for v in dependency.values():
        if selected in v:
            v.remove(selected)

print 'Answer', ''.join(result)

# results
# Answer BCEFLDMQTXHZGKIASVJYORPUWN
