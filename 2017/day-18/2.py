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

contexts = [
    # 0
    {
        'registers': {'p': 0},
        'loc': 0,
        'in_queue': [],
        'wait': False,
    },

    # 1
    {
        'registers': {'p': 1},
        'loc': 0,
        'in_queue': [],
        'wait': False,
    },
]


def set_value(context, name, value):
    context['registers'][name] = value

def get_value(context, r1):
    if isinstance(r1, str):
        return context['registers'].get(r1, 0)
    return r1


ctx = 0
snd_ctr = [0, 0]


while True:
    ctx2 = (ctx + 1) % 2
    context = contexts[ctx]

    if contexts[ctx]['wait'] and contexts[ctx2]['wait']:
        print 'Both in wait - exit'
        break

    cmd_line = commands[context['loc']]
    cmd = cmd_line[0]

    # print
    # print '%1d#%02d: %s' % (ctx, context['loc'], cmd)

    if cmd == 'set':
        set_value(context, cmd_line[1], get_value(context, cmd_line[2]))

    elif cmd == 'add':
        v = get_value(context, cmd_line[1]) + get_value(context, cmd_line[2])
        set_value(context, cmd_line[1], v)

    elif cmd == 'mul':
        v = get_value(context, cmd_line[1]) * get_value(context, cmd_line[2])
        set_value(context, cmd_line[1], v)

    elif cmd == 'mod':
        v = get_value(context, cmd_line[1]) % get_value(context, cmd_line[2])
        set_value(context, cmd_line[1], v)

    elif cmd == 'snd':
        v = get_value(context, cmd_line[1])
        # print '\tSND v=%d ' % v
        contexts[ctx2]['in_queue'].append(v)
        contexts[ctx2]['wait'] = False
        snd_ctr[ctx] += 1

    elif cmd == 'rcv':
        if len(context['in_queue']) == 0:
            # print '\tRCV => wait'
            context['wait'] = True
            ctx = (ctx + 1) % 2
            continue

        # print '\tRCV => get'
        v = context['in_queue'][0]
        context['in_queue'] = context['in_queue'][1:]
        set_value(context, cmd_line[1], v)

    elif cmd == 'jgz':
        x = get_value(context, cmd_line[1])
        y = get_value(context, cmd_line[2])
        if x > 0:
            # print '\tJGZ x=%d => jump on %d loc' % (x, y)
            context['loc'] += y
            continue
        else:
            pass
            # print '\tJGZ x=%d => skip' % x

    # next
    context['loc'] += 1
    if context['loc'] >= len(commands):
        print 'Error: out of mem'
        break




print 'Finish!!'
print '000000'
print 'registers:', contexts[0]['registers']
print 'in_queue:', contexts[0]['in_queue']
print
print '111111'
print 'registers:', contexts[1]['registers']
print 'in_queue:', contexts[1]['in_queue']
print
print 'snd_ctr', snd_ctr
