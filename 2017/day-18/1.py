#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
# data_lines = [
#     'set a 1',
#     'add a 2',
#     'mul a a',
#     'mod a 5',
#     'snd a',
#     'set a 0',
#     'rcv a',
#     'jgz a -1',
#     'set a 1',
#     'jgz a -2'
# ]

commands = [line.split() for line in data_lines]
data_lines = None

# parse int const
for cmd_line in commands:
    for x in xrange(1,len(cmd_line)):
        arg = cmd_line[x]
        if (len(arg) != 1) or (ord(arg) < ord('a')):
            cmd_line[x] = int(arg)

registers = {}

def set_value(name, value):
    registers[name] = value

def get_value(r1):
    if isinstance(r1, str):
        return registers.get(r1, 0)
    return r1


loc = 0
freq = None

while True:
    cmd_line = commands[loc]
    cmd = cmd_line[0]
    # print
    # print registers
    # print '%02d: %s' % (loc, cmd)

    if cmd == 'set':
        set_value(cmd_line[1], get_value(cmd_line[2]))

    elif cmd == 'add':
        v = get_value(cmd_line[1]) + get_value(cmd_line[2])
        set_value(cmd_line[1], v)

    elif cmd == 'mul':
        v = get_value(cmd_line[1]) * get_value(cmd_line[2])
        set_value(cmd_line[1], v)

    elif cmd == 'mod':
        v = get_value(cmd_line[1]) % get_value(cmd_line[2])
        set_value(cmd_line[1], v)

    elif cmd == 'snd':
        freq = get_value(cmd_line[1])
        print '\tSND freq=%d ' % freq

    elif cmd == 'snd':
        freq = get_value(cmd_line[1])

    elif cmd == 'rcv':
        v = get_value(cmd_line[1])
        if v == 0:
            print '\tRCV 0 => skip'
        else:
            print '\tRCV %d => Finish' % v
            break

    elif cmd == 'jgz':
        x = get_value(cmd_line[1])
        y = get_value(cmd_line[2])
        if x > 0:
            print '\tJGZ x=%d => jump on %d loc' % (x, y)
            loc += y
            continue
        else:
            print '\tJGZ x=%d => skip' % x

    # next
    loc += 1
    if loc >= len(commands):
        print 'Error: out of mem'
        break


print 'Finish!!'

print 'registers:', registers
print 'freq:', freq
