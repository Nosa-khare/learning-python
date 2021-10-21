
"""
A scenario where it would be important to use a class variable, would be when 
 an attribute is to have a constant value across all instances. This can then be 
 referenced in a class method
e.g a total number of employees (num_of_emps) which increases each time a new 
 employee is created.
"""


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
    
    @classmethod
    def count(cls):
        return cls.num_of_emps


print('Employee count:', Employee.count())

print('\nCreating two employees...')
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('John', 'Smith', 60000)
print('Employee count now:', Employee.num_of_emps)

print('\nCreating one more employee...')
emp_3 = Employee('Jane', 'Jones', 50000)
print('Employee count now:', emp_1.num_of_emps)
