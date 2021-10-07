"""
Tuples can have all lists methods that do not invlove altering its state.

they can be looped through, enumurated, e.t.c.
"""

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')

for i, e in enumerate(tuple_1, start=1):
    print(i, e)
