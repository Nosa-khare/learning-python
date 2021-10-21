# instance methods and variables
"""
--Instance variables are used to store data that is unique to each instances
--
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
emp_2 = Employee('John', 'Smith', 60000)

print(emp_1.fullname())

"""
Methods can also be run from the class name itself.
In this case the instance has to be passed into the method as an argument
It enables the class know what instance the method should be called upon
"""
print(Employee.fullname(emp_2))
