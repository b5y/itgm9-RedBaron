from __future__ import print_function

import ast

from redbaron import RedBaron

code = """
class foo(object):
    def bar():
        print 'Do you like Vodka?'
"""

red = RedBaron(code)

print("This is RedBaron tree:")
print(red.help(with_formatting=True))


tree = ast.parse(code)

print("\nThis is Python AST:\n")


print(ast.dump(tree))
