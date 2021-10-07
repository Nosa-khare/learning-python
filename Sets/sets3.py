l1 = [1, 2, 3, 1, 2, 3]

# a set function can be used make a new list with no duplicates

l2 = list(set(l1))

print(l1)
print(l2)

employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']


# To find employees who are both gym_memberse and developers:
result1 = set(gym_members).intersection(developers)
print(result1)
# note: the object using the intersection() method must be a set,
#  while the other being compared to can be a list or a set

# To find employees who are neither gym_members or developers:
result2 = set(employees).difference(developers, gym_members)
print(result2)


# Membership Tests
"""Sets are optimized for membership tests"""

if 'Corey' in developers:  # list
    print('Found!')

if 'Corey' in set(developers):  #set
    print('Found!')

# O(n) for List
# O(1) for Sets