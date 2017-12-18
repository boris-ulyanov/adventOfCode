#!/usr/bin/python

progs_size = 16

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
# progs_size = 5
# data_lines = ['s1,x3/4,pe/b']

progs = [ chr(x + ord('a')) for x in xrange(progs_size)]
commands = data_lines[0].split(',')
data_lines = None

print 'Start:', ''.join(progs)

for cmd in commands:
    c = cmd[0]
    # print cmd

    if c == 's':
        n = int(cmd[1:])
        # print '  => spin', n
        # print '     pre', progs
        progs = progs[-n:] + progs[:-n]
        # print '     aft', progs

    elif c == 'x':
        p = (cmd[1:]).split('/')
        n1 = int(p[0])
        n2 = int(p[1])
        # print '  => exchange', n1, n2
        # print '     pre', progs
        t = progs[n1]
        progs[n1] = progs[n2]
        progs[n2] = t
        # print '     aft', progs

    elif c == 'p':
        p = (cmd[1:]).split('/')
        # print '  => partner', p[0], p[1]
        # print '     pre', progs
        n1 = progs.index(p[0])
        n2 = progs.index(p[1])
        t = progs[n1]
        progs[n1] = progs[n2]
        progs[n2] = t
        # print '     aft', progs

print 'Finish: ', ''.join(progs)
