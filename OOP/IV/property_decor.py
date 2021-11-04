# Using the property decorator

"""
This allows to give class attributes getter, setter and deleter functionalities
"""


class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

    def fullname(self):
        return f'{self.first_name} {self.last_name}'


emp_1 = Employee('Corey', 'Schafer', 50000)

print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname())

emp_1.first_name = "John"

print()
print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname())

"""
We notice that even after changing the first name, the email doesn't make the same change 
 because it is determined by the first_name value passed into the init method

A fix for this would be to make the email a method instead of an attribute, this way any 
 changes made to the name attributes would be accessible by the email method.
This has to be done without breaking the rest of the code, specifically in areas where the email
is already being referenced as an attribute and not a function call

This is where the property decorator comes in
"""
