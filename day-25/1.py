#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
# data_lines = [
#     'Begin in state A.',
#     'Perform a diagnostic checksum after 6 steps.',
#     '',
#     'In state A:',
#     '  If the current value is 0:',
#     '    - Write the value 1.',
#     '    - Move one slot to the right.',
#     '    - Continue with state B.',
#     '  If the current value is 1:',
#     '    - Write the value 0.',
#     '    - Move one slot to the left.',
#     '    - Continue with state B.',
#     '',
#     'In state B:',
#     '  If the current value is 0:',
#     '    - Write the value 1.',
#     '    - Move one slot to the left.',
#     '    - Continue with state A.',
#     '  If the current value is 1:',
#     '    - Write the value 1.',
#     '    - Move one slot to the right.',
#     '    - Continue with state A.',
# ]


states = {}

for idx in xrange(3, len(data_lines), 10):

    s = data_lines[idx]
    state = s[9]

    s = data_lines[idx + 2]
    val0 = int(s[22])
    s = data_lines[idx + 3]
    move0 = -1 if s[27] == 'l' else 1
    s = data_lines[idx + 4]
    next0 = s[26]

    s = data_lines[idx + 2 + 4]
    val1 = int(s[22])
    s = data_lines[idx + 3 + 4]
    move1 = -1 if s[27] == 'l' else 1
    s = data_lines[idx + 4 + 4]
    next1 = s[26]

    states[state] = [[val0, val1], [move0, move1], [next0, next1]]

data_lines = None


for s in states:
    print s, states[s]

state = 'A'
tape = [0]
position = 0
negatives = 0

for step in xrange(12667664 ):
    value = tape[negatives + position]

    s = states[state]

    new_value = s[0][value]
    new_move = s[1][value]
    new_state = s[2][value]

    tape[negatives + position] = new_value

    position += new_move

    if (negatives + position) >= len(tape):
        tape = tape + [0]
    elif position < -negatives:
        tape = [0] + tape
        negatives += 1

    state = new_state


checksum = 0
for v in tape:
    checksum += v

print 'tape', tape
print 'checksum', checksum
print 'position', position
print 'negatives', negatives

