"""
Inheritance allows to inherit attributes and methods from a parent class.
 Subclasses can be created and get all of the functionality from the parent
 class and also override and add new functionalities without affecting the 
 parent class in any way.
"""


# Parent class
class Employee:
    num_of_emps = 0
    raise_amount = 1.04  # 4% increase

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

        Employee.num_of_emps += 1  # have an increase of 1 at every new instance

    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount


# To create new types of employees (Developers and Managers)
"""
These types of employees will have the same attributes of the Employee class,
but will have even more others, hence inheritance
"""


class Developer(Employee):
    pass


# Even without any code of its own, the developer class already has all of the attributes
# and methods contained in the Employee class

dev_1 = Developer('Corey', 'Schafer', 50000)
dev_2 = Developer('John', 'Smith', 60000)

"""
When the dev_1 and dev_2 objects were instantiated, python first looked into the 
 developer class for the __init__().
 When not found, it then went down the chain of its inheritance (method resolution order) 
 till found in the Employee class.
"""
# print(help(Developer))  # To check order and other details

print(dev_1.fullname())
print(dev_2.email)
