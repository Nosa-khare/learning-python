# Setter & deleter
# Read extensively about concepts


"""
A setter would be ideal To give a property the ability to be updated to a value, and then use that value to in 
 turn update other existing attributes that are connected to it (either are dependent, or it depends on)

While a deleter would be used in the same way. But instead of updating, it would enable values to be deleted
 by setting the attributes to None.

E.g using the fullname property to update and delete the first_name and last_name attributes
"""


class Employee:
    num_of_emps = 0
    raise_amount = 1.04  # 4% increase

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@email.com'

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    
    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name
    
    @fullname.deleter
    def fullname(self):
        self.first_name = None
        self.last_name = None
        print('Name deleted!')


emp_1 = Employee('Corey', 'Schafer', 50000)

print(emp_1.first_name)
print(emp_1.fullname)
print(emp_1.email)

del emp_1.fullname

print(emp_1.first_name) 
