#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

from redbaron import RedBaron

with open("input_file.py", 'rb') as fd:
    source = fd.read()

red = RedBaron(source_code=source)

functions = red.find_all('DefNode')

print("\nMethod's names:")
map(lambda x: print(x.name), functions)

classes = red.find_all('ClassNode')

print("Class's names:\n")
map(lambda x: print(x.name), classes)

print("\nIndentations:")
map(lambda x: print(len(x.indentation)), functions.data)
