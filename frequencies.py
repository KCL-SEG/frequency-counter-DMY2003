"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here=]
    for x in items:
        x = str(x)
        frequencies[x] = 0
    for i in items:
        i = str(i)
        frequencies[i] = frequencies[i] + 1
    return frequencies
