student = {
    'name': 'John',
    'age': '25',
    'courses': ['Math','ComSci'],
    'phone': '555-5555'
    }

print(student,'\n')

print('No of items in the dictionary:', len(student),'\n')

print('Keys list:', list(student.keys()),'\n')

print('Values list:', list(student.values()),'\n')

print('Items list:', list(student.items()),'\n')

#Looping through

for key in student.keys():
    print(key)

print()

for key, value in student.items():
    print(key, ',', value)
    