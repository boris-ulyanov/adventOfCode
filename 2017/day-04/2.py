#!/usr/bin/python


def check_phrase(words):
    sorted_words = [''.join(sorted(w)) for w in words]

    uniq_words = set(sorted_words)

    if len(words) == len(uniq_words):
        return 1
    else:
        return 0


data_file = open('./data', 'r')
lines = data_file.readlines()
data_file.close()

result = 0

for line in lines:
    words = line.split()
    uniq_words = set(words)
    if len(words) == len(uniq_words):
        result += check_phrase(words)

print result
