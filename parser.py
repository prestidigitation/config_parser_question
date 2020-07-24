#!/usr/bin/env python
from pathlib import Path

path = 'config/example.txt'
with open(path, 'r') as f:
    data = f.readlines()

valid_parameters = [
    'host',
    'server_id',
    'server_load_alarm',
    'user',
    'verbose',
    'test_mode',
    'debug_mode',
    'log_file_path',
    'send_notifications'
]

parsed_lines = []
for line in data:
    # skip commented lines
    if line[:1] == '#':
        continue
    # strip out all whitespace
    trimmed_line = ''.join(line.split())
    parsed_line = trimmed_line.split('=')
    # skip erroneous lines
    if parsed_line[0] not in valid_parameters:
        continue
    parsed_lines.append(parsed_line)

