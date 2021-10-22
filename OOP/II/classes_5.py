"""
Regular methods in a class automatically take in the instance as the first
arguament when they are called (self).
Class methods automatically take in the class as the first argument when it
is called (cls).
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
    def set_raise_amnt(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def count(cls):
        return cls.num_of_emps


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('John', 'Smith', 60000)

Employee.set_raise_amnt(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


"""
Class methods can also be run from instances as well, but that would
not make much sense.
"""
emp_1.set_raise_amnt(1.09)
print('\nRunning from an insstance...')  # still keeps constant accross entire class
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
