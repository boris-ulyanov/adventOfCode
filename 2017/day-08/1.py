#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

instructs = [line.split() for line in data_lines]
data_lines = None


regs = {}


for instr in instructs:

    reg_name = instr[0]
    reg_operator = instr[1]
    reg_const_value = int(instr[2])

    cond_operand_name = instr[4]
    cond_operator = instr[5]
    cond_const_value = int(instr[6])

    cond_result = None
    cond_operand_value = regs.get(cond_operand_name, 0)

    if cond_operator == '<':
        cond_result = cond_operand_value < cond_const_value
    elif cond_operator == '<=':
        cond_result = cond_operand_value <= cond_const_value
    elif cond_operator == '==':
        cond_result = cond_operand_value == cond_const_value
    elif cond_operator == '!=':
        cond_result = cond_operand_value != cond_const_value
    elif cond_operator == '>':
        cond_result = cond_operand_value > cond_const_value
    elif cond_operator == '>=':
        cond_result = cond_operand_value >= cond_const_value
    else:
        print 'Error: unexpected cond_operator = [%s]', cond_operator

    if not cond_result:
        continue

    if reg_operator == 'inc':
        regs[reg_name] = regs.get(reg_name, 0) + reg_const_value
    elif reg_operator == 'dec':
        regs[reg_name] = regs.get(reg_name, 0) - reg_const_value
    else:
        print 'Error: unexpected reg_operator = [%s]', reg_operator


print 'Max value:', max(regs.values())
