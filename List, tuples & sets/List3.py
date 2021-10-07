courses = ['Python', 'SQL', 'Docker', 'Airflow', 'NoSQL']
nums = [1, 5, 3, 4, 2]
print('Courses:', courses)
print('Numbers:', nums)

courses.reverse()
print('Reversed courses list:', courses)

courses.sort()
nums.sort()
print('Sorted courses list:', courses)
print('Sorted nums list:', nums)

courses.sort(reverse=True)
nums.sort(reverse=True)
print('Reverse sorted courses list:', courses)
print('Reverse sorted nums list:', nums)


courses_sorted = sorted(courses)  # this works like the .sort, but it doesn't alter the original list
print('New sort method:', courses_sorted)


