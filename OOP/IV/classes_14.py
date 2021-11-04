"""
To give the Employee class the ability for its objects to be added up, we use
 the __add__ method.

The  addition of employee objects would mean the pay of each be added together
 this is not a proper way to operate in real code. It's always best to be explicit 
 about what's being added
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
    

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('John', 'Smith', 60000)

print(emp_1 + emp_2)

print(emp_1.__add__(emp_2))
