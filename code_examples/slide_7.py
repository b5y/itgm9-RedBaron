#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

from redbaron import RedBaron

with open("input_file.py") as fd:
    source = fd.read()

red = RedBaron(source_code=source)

functions = red.find_all('DefNode')

print("\nClasses:")
for function in functions:
    print(function.name)

classes = red.find_all('ClassNode')

print("Methods:\n")
for class_ in classes:
    print(class_.name)
