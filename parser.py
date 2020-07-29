#!/usr/bin/env python

import sys

path = 'config/example.txt'
with open(path, 'r') as f:
    # read in all data from file at once. Would need refactoring to read line by line for massive files
    data = f.readlines()

parameters_schema = {
    'host': str,
    'server_id': str,
    'server_load_alarm': float,
    'user': str,
    'verbose': bool,
    'test_mode': bool,
    'debug_mode': bool,
    'log_file_path': str,
    'send_notifications': bool
}

def convert_to_bool(string):
    conversion_dict = {
        'true': True,
        'false': False,
        'yes': True,
        'no': False,
        'on': True,
        'off': False
    }
    try:
        return conversion_dict[string]
    except KeyError:
        print('Could not convert value to bool: value not in conversion dictionary.')

parsed_lines = []
for line in data:
    # skip commented lines
    if line[:1] == '#':
        continue
    # strip out all whitespace
    trimmed_line = ''.join(line.split())
    parsed_line = trimmed_line.split('=')
    # skip erroneous lines
    if parsed_line[0] not in parameters_schema:
        continue
    parsed_lines.append(parsed_line)

hashed_data = {}
for key, value in parsed_lines:
    if parameters_schema[key] is bool:
        # check if parameter should have a boolean value and try to add it to hash, otherwise skip it
        hashed_data[key] = convert_to_bool(value)
    elif key == 'server_load_alarm':
        # throws error if float conversion fails
        hashed_data[key] = float(value)
    else:
        # add remaining string-based key/value pairs to hash
        hashed_data[key] = value

print(hashed_data)
