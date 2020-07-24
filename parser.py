#!/usr/bin/env python
from pathlib import Path

path = 'config/example.txt'
with open(path, 'r') as f:
    data = f.readlines()

for line in data:
    # skip commented lines
    if line[:1] == '#':
        continue
    # strip out all whitespace
    trimmed_line = ''.join(line.split())
    parsed_line = trimmed_line.split('=')
    # print(parsed_line)