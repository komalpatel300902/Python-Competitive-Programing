"""Wraping the text in Perticural width."""

import textwrap

def wrap(string, max_width):
    str = ''
    for x in range(0,len(string)):
        if x != 0 and x%(max_width) == 0:
            str += "\n"
        str += string[x] 
    return str

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

