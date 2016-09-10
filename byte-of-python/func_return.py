#!/usr/bin/python
# FileName : func_return.py

def maximum(x, y):
    if x > y:
        return x
    else:
        return y

x = raw_input('Enter a number:')
y = raw_input('Enter a another number:')
print maximum(x, y)
