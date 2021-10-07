
courses = ['Python', 'SQL', 'Docker', 'Airflow', 'NoSQL']
print('Courses:', courses)

print(courses.index('SQL'))  # Fetch index of item in a list

print(min(courses))  # aggregates

print('Python' in courses)  # returns a boolean

print("Traditional indexing:")
for index, course in enumerate(courses):
    print(f"{index}, {course}")

print("\nCustomized indexing")
for index, course in enumerate(courses, start=1):
    print(f"{index}, {course}")


courses_string = ", ".join(courses)
print(courses_string)

newlist = courses_string.split(', ')
