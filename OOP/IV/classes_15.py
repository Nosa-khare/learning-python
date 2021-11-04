"""
To enable the Employee objects have the len function operate, the __len__ method can be used.

This cann be set to return the total number characters in the employee's fullname
"""


class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    
    def __repr__(self) -> str:
        """
        Best practice is to have the __repr__() return/output a string that can be 
        used to recreate the object
        """
        return f'Employee({self.first_name}, {self.last_name}, {self.pay},)'
    
    def __str__(self) -> str:
        return f'{self.fullname()}: {self.email}'
    
    def __add__(self, other):
        return self.pay + other.pay 

    def __len__(self):
        return len(self.fullname())
    

emp_1 = Employee('Corey', 'Schafer', 50000)

print(len(emp_1))
print(emp_1.__len__())
