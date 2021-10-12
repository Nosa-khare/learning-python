# delete key and value from the dictionary

student = {
    'name': 'John',
    'age': '25',
    'courses': ['Math','ComSci'],
    'phone': '555-5555'
    }

print(student,'\n')

del student['age']
print(student, '\n')

courses = student.pop('courses')  # deletes item from the dictionnary and returns it.
print('Courses: ', courses, '\n')

print(student)
