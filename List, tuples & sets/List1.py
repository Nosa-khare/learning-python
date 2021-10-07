courses = ['python', 'SQL', 'Docker', 'Airflow', 'NoSQL']

print(courses)

print('First item:', courses[0])

print('Last item:', courses[-1])

print('First two items:', courses[0:2])
print('First two items:', courses[:2])

print('Last two items:', courses[-2:])

courses.append('Flask')  # Add an item to an existing list
print(courses)

courses.insert(0, 'CompSci' )  # Add item to a specific location of an existing list
print(courses)


