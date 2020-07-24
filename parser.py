#!/usr/bin/env python
from pathlib import Path

path = 'config/example.txt'
with open(path, 'r') as f:
    data = f.readlines()

for line in data:
    print(line)