cs_courses = {'Hitsory', 'Math', 'Physics', 'CompSci'}

print(cs_courses)  # Unordered output is printed out

# Add duplicate value
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print(cs_courses)  # Sets remove duplicate vaues


# Membership test
print('CompSci' in cs_courses)  # Sets are optimized for this operation than lists/tuples

art_courses = {'History', 'Math', 'Fine Art', 'Design'}

print(cs_courses.intersection(art_courses))

print(cs_courses.difference(art_courses))

print(art_courses.difference(cs_courses))

print(art_courses.union(cs_courses))
