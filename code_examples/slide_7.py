#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

from redbaron import RedBaron

with open("input_file.py") as fd:
    source = fd.read()

red = RedBaron(source_code=source)

functions = red.find_all('DefNode')

print("\nClasses:")
map(lambda x: print(x.name), functions)

classes = red.find_all('ClassNode')

print("Methods:\n")
map(lambda x: print(x.name), classes)
