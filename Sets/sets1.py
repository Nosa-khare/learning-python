# create empty set

s1 = {}  # empty dictionary not empty set
s1 = set()  # empty set
s2 = {9, 8, 0}
s1.update([1, 2, 3, 4, 5], s2)  # updates the set with the supplied values
print(s1, '\n')

s1.remove(5)
print(s1, '\n')

s1.discard(5)  # performs same functions as remove, but doesn't throw errors for non-existent values
s1.remove(5)  # throws key error as 5 is not in set