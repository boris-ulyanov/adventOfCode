#!/usr/bin/python

import sys
from collections import defaultdict

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

N_WORKERS = 5
ADDED_TIME = 60

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
    N_WORKERS = 2
    ADDED_TIME = 0

data = [ tuple([line[5:6], line[36:37]]) for line in data_lines]
data_lines = None
data_len = len(data)

# make dependency
dependency = defaultdict(list)
for d in data:
    dependency[d[1]].append(d[0])
    dependency[d[0]]

log = []
total_time = 0
workers_busy = [0] * N_WORKERS
workers_task = []
workers_task = ['.'] * N_WORKERS

while len(dependency) > 0:
    # select possible task
    may_be_done = []
    for k, v in dependency.items():
        if len(v) == 0:
            may_be_done.append(k)

    may_be_done.sort()
    # print 'may_be_done', may_be_done

    for task in may_be_done:
        if not 0 in workers_busy:
            break   # no free workers

        # apply task to worker
        free_worker_idx = workers_busy.index(0)
        # print 'apply', task, 'to', free_worker_idx, 'worker'
        workers_task[free_worker_idx] = task
        workers_busy[free_worker_idx] = ord(task) - ord('A') + 1 + ADDED_TIME
        dependency[task].append('in progress')

    # end tasks or workers

    # select shortest task
    shortest_task_value = 0
    shortest_task_idx = -1
    for i in xrange(N_WORKERS):
        if workers_busy[i] == 0:
            continue
        if (shortest_task_idx == -1) or (workers_busy[i] < shortest_task_value):
            shortest_task_idx = i
            shortest_task_value = workers_busy[i]

    assert(shortest_task_idx >= 0)

    # print 'shift on', shortest_task_value, 'sec'

    for _ in xrange(shortest_task_value):
        log.append(workers_task[:])

    # shift on shortest_task_value
    for i in xrange(N_WORKERS):
        if workers_busy[i] == 0:
            continue
        workers_busy[i] -= shortest_task_value

        # mark task as done
        if workers_busy[i] == 0:
            task_done = workers_task[i]
            # print 'task_done', task_done
            workers_task[i] = '.'
            del dependency[task_done]
            for v in dependency.values():
                if task_done in v:
                    v.remove(task_done)

    total_time += shortest_task_value
    # >>>>>>>> FINISH all tasks


for l in log:
    print l

print 'Answer', total_time

# results
# Answer 15/987
