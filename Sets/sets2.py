s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

s4 = s1.intersection(s2)  # values common in s2 and s1
print(s4)

s5 = s1.intersection(s2, s3)  # first intersect s2 & s3, then intersects the result set with s1
print(s5)


# Differences

s6 = s1.difference(s2)
print(s6)  # displays values in s1, not in s2

s7 = s1.difference(s2, s3)
print(s7)  # displays values in s1, not in s2 nor s3

## symmetric difference
s8 = s1.symmetric_difference(s2)
print(s8)  # prints all differences between both sets

