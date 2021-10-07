courses = ['python', 'SQL', 'Docker']
print('Courses:', courses)

courses_2 = ['Airflow', 'CompSci', 'NoSQL']

courses.extend(courses_2)
print('Extended courses:', courses)

courses.remove('CompSci')
print('Removed CompSci:', courses)

popped = courses.pop(3)  # If no specified index in the pop method, the last item  on the list is popped
print('Popped value:', popped, '\nNew list:', courses)
