# Special dunder (magic) methods

"""
These special methods allows to emulate / alter some built-in behaviour within python,
 and also implement operator overloading.

For example;
"""

print(1 + 2)
print('a' + 'b')

"""
We see that the add operation behaves differently for the two different datatype.
Sums up for int
Concatenates for strings
"""


class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

        Employee.num_of_emps += 1  # have an increase of 1 at every new instance

    def fullname(self):
        return f'{self.first_name} {self.last_name}'


emp_1 = Employee('Corey', 'Schafer', 50000)
print(emp_1)

""""
Printing emp_1 returns the vague object info, This is not a user friendly 
 information
This behaviour can also be changed using the  special dunder methods 
 "__repr__" and "__str__"
"""
# __repr__: This is an unambiguous representation of the object, to be used for
# debugging and logging. Its meant to be seen by developers

# __str__: This is a more readable representation of the object to be displayed
# to end user.

"""
NOTE: It is important to have at least the __repr__ method defined. This when the 
 __str__ method is called on the object, even without it being predefined (existing), python 
 falls back to the __repr__ method.
"""
