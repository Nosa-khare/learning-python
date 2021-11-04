# Adding special methods to the Employee class

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


emp_1 = Employee('Corey', 'Schafer', 50000)

print(emp_1)  # By default returns the __str__() operation

print(repr(emp_1))  # returns the __repr__() operation specifically
print(str(emp_1))  # returns the __str__() operation specifically

"""
What really happens is, python calls the __repr__ and __str__ methods on the employee
object.
"""
# print(emp_1.__repr__())
# print(emp_1.__str__())
