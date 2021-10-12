student = {
    'name': 'John',
    'age': '25',
    'courses': ['Math','ComSci']
    }

print(student, '\n')  # prints out the dictionary content

print(student['name'], '\n')  # print out a specific item

#print(student['phone'])  # throws error, phone doesn't exist in the dictionary


""" the .get() method can be used to prevent errors when fetching a non-exixtent
item from a dictionary"""

print(student.get('phone'))  # prints none
print(student.get('phone', 'Not found'), '\n')  # prints out default value 'Not found'


# add new item/ update existing value to the dictionary
student['phone'] = '555-5555'
student['name'] = 'Jane'

print(student, '\n')


# batch update using update() method'
student.update({'name': 'John', 'age': 26, })
print('Update: ', student)