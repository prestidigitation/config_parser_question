#!/usr/bin/env python

import sys

path = 'config/example.txt'
with open(path, 'r') as f:
    # read in all data from file at once. Would need refactoring to read line by line for massive files
    data = f.readlines()

parameters_schema = {
    'host': 'str',
    'server_id': 'str',
    'server_load_alarm': 'float',
    'user': 'str',
    'verbose': 'bool',
    'test_mode': 'bool',
    'debug_mode': 'bool',
    'log_file_path': 'str',
    'send_notifications': 'bool'
}

bool_conversion_schema = {
    'true': True,
    'false': False,
    'yes': True,
    'no': False,
    'on': True,
    'off': False
}

def str_splitter(string):
    # split string into list of strings delimited by first instance of '=' character. Cannot handle key names containing '='
    delimited_str_list = string.split('=', 1)
    # strip out leading and trailing whitespace from strings in list
    stripped_str_list = [x.strip() for x in delimited_str_list]
    return stripped_str_list

def convert_to_bool(string, schema_dict):
    try:
        return schema_dict[string]
    except KeyError:
        print('Could not convert value to bool: value not in conversion dictionary.')

def str_converter(string, schema_type):
    if schema_type == 'str':
        return string
    elif schema_type == 'bool':
        return convert_to_bool(string, bool_conversion_schema)
    elif schema_type == 'int':
        return int(string)
    elif schema_type == 'float':
        return float(string)

hashed_data = {}
for line in data:
    # skip commented lines. Slice operator will not throw IndexError exception for empty strings
    if line[:1] == '#':
        continue
    # split line into key/value strings
    parsed_line = str_splitter(line)
    try:
        key, value = parsed_line
    except ValueError:
        print('There should only be two items in the list: one key and one value')
    try:
        key in parameters_schema
    except KeyError:
        print('Key not found in parameters schema.')
    converted_value = str_converter(value, parameters_schema[key])
    hashed_data[key] = converted_value

# Debugging
for key, value in hashed_data.items():
    print(f"{key}: {value}")

print(hashed_data)
