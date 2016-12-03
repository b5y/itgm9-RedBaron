#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

from redbaron import RedBaron

with open("input_file.py", 'rb') as fd:
    source = fd.read()

red = RedBaron(source_code=source)

functions = red.find_all('DefNode')
specific_function = red.find('DefNode', name='buzzy')
print('Buzzy node:')
print(specific_function.dumps())

print("Renaming function")
for function in functions:
    if function.name == 'buzzy' or function.name == 'bar':
        function.name = 'new_' + function.name

print(red.dumps())
