# class variables and methods
"""
Class variables are variables shared among all instances of a class.

--when we access class variables, it needs to be accessed through the 
  class themselves (class.variable) or an instance of the class (self.variable).
  Hence the self attribute must be suffixed to the variable name.
"""


class Employee:

    raise_amount = 1.04  # 4% increase

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    
    def apply_raise(self):
        self.pay = self.pay * self.raise_amount


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('John', 'Smith', 60000)

# Now we can access the variable
print(Employee.raise_amount)  # accessing through the class
print(emp_1.raise_amount)  # Accessing through an instance


"""
When a class variable is accessed through an instance, it first checks if
 if the instance has such attribute, if not, it then checks if the class, or any
 it inherits from has the attribute

This can be understood by printing the name spaces.
    Employee.__dict__
    emp_1.__dict__
"""

print(emp_1.__dict__)  # emp_1 has no attribute raise_amount
print(Employee.__dict__)  # the Employee class has the attribute, instances can have
# access to the attribute
