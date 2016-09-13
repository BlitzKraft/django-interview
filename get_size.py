#! /usr/bin/python

import re

all_sizes = []
all_count = []

def image_size(s):
    out = re.findall('\d+x\d+', s)
    return out[-1]

with open('fun-rooster-thumbnail-names.txt') as test:
    content = test.readlines()
    for ln in content:
        matches = image_size(ln)
        if matches in all_sizes:
            all_count[all_sizes.index(matches)] += 1
        else:
            all_sizes.append(matches)
            all_count.append(1)
        # print "Matches = " + matches

for i in range(len(all_sizes)):
    print all_sizes[i] + " thumbnail occurs " + str(all_count[i]) + " times"

