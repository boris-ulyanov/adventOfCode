#!/usr/bin/python

progs_size = 16

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
# progs_size = 5
# data_lines = ['s1,x3/4,pe/b']

ASCII_A = ord('a')

shuffles = [x for x in xrange(progs_size)]
replaces = [ chr(x + ASCII_A) for x in xrange(progs_size)]

commands = data_lines[0].split(',')
data_lines = None


for cmd in commands:
    c = cmd[0]

    if c == 's':
        n = int(cmd[1:])
        shuffles = shuffles[-n:] + shuffles[:-n]

    elif c == 'x':
        p = (cmd[1:]).split('/')
        n1 = int(p[0])
        n2 = int(p[1])
        t = shuffles[n1]
        shuffles[n1] = shuffles[n2]
        shuffles[n2] = t

    elif c == 'p':
        p = (cmd[1:]).split('/')
        n1 = replaces.index(p[0])
        n2 = replaces.index(p[1])
        t = replaces[n1]
        replaces[n1] = replaces[n2]
        replaces[n2] = t

commands = None

for i in xrange(progs_size):
    replaces[i] = ord(replaces[i]) - ASCII_A

# progs = [ chr(x + ASCII_A) for x in xrange(progs_size)]
progs = [x for x in xrange(progs_size)]

print 'Start:',
# print 'Progs', ''.join(progs)
print 'Progs', progs
print 'Shuffles', shuffles
print 'Replaces', replaces

tmp = [0 for x in xrange(progs_size)]

for x in xrange(1000000):

    for i in xrange(progs_size):
        tmp[i] = progs[shuffles[i]]

    for i in xrange(progs_size):
        progs[i] = replaces[tmp[i]]


for i in xrange(progs_size):
    progs[i] = chr(progs[i] + ASCII_A)

print 'Finish'
print ''.join(progs)
