#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

nodes = {}

for line in data_lines:
    chunks = line.split()
    name = chunks[0]
    node = {'weight' : int(chunks[1][1 : -1])}
    if len(chunks) > 2:
        node['childs'] = ''.join(chunks[3:]).split(',')
    nodes[name] = node

data_lines = None

for name in nodes:
    node = nodes[name]
    if 'childs' in node:
        for child_name in node['childs']:
            child = nodes[child_name]
            child['parent'] = name

root = ''

for name in nodes:
    node = nodes[name]
    if 'parent' not in node:
        root = name
        print 'root:', root


def nodeWeight(nodeName):
    node = nodes[nodeName]
    selfWeight = node['weight']

    if not 'childs' in node:
        node['fullWeight'] = selfWeight
        return selfWeight

    # has childs
    childsWeights = [ nodeWeight(child) for child in node['childs'] ]

    if max(childsWeights) != min(childsWeights):
        print 'Disbalance!!!'
        print '\t root name:', nodeName
        print '\t selfWeight:', selfWeight
        print '\t childsWeights:', childsWeights

        print '\t childs:'
        for child in node['childs']:
            print '\t - %10s    full:%8d    self:8%d' % (child, nodes[child]['fullWeight'], nodes[child]['weight'])

    fullWeight = selfWeight + sum(childsWeights)
    node['fullWeight'] = fullWeight
    return fullWeight


print 'root weight:', nodeWeight(root)
