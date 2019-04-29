#! /usr/bin/env python
from lndynamic import LNDynamic


with open(r"/home/hme/commands.txt") as hpass:
    lines = hpass.readlines()

api = LNDynamic(lines[0].rstrip('\n'), lines[1].rstrip('\n'))
results = api.request('vm', 'list')
print(results)
