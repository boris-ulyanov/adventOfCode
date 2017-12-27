#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

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

counter = 0

while True:
    if loc >= len(commands):
        print 'Error: loc outranged:', loc
        break

    cmd_line = commands[loc]
    cmd = cmd_line[0]
    # print
    # print registers
    # print '%02d: %s' % (loc, cmd)

    if cmd == 'set':
        set_value(cmd_line[1], get_value(cmd_line[2]))

    elif cmd == 'sub':
        v = get_value(cmd_line[1]) - get_value(cmd_line[2])
        set_value(cmd_line[1], v)

    elif cmd == 'mul':
        v = get_value(cmd_line[1]) * get_value(cmd_line[2])
        set_value(cmd_line[1], v)
        counter += 1

    elif cmd == 'jnz':
        x = get_value(cmd_line[1])
        y = get_value(cmd_line[2])
        if x != 0:
            print '\tJNZ x=%d => jump on %d (%d=>%d) loc' % (x, y, loc, loc + y)
            loc += y
            continue
        else:
            print '\tJNZ x=%d => skip' % x

    else:
        print 'Unrecognized cmd:', cmd

    # next
    loc += 1


print 'Finish!!'

print 'registers:', registers
print 'counter:', counter
