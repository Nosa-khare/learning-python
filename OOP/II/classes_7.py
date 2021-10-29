"""
-Regular methods in a class automatically take in the instance as the first
 arguament when they are called (self).
-Class methods automatically take in the class as the first argument when it
 is called (cls).

-Static methods do not take in anything at all. They connect to the class not in 
 code, but do so in logic and concept. They are regular funnctions which could
 exist normally would be outside the class, but are defined within the class for
 structural / organosational reasons.

 For example a simple function to collect a date and return whether or not is
 is a workday.
 this kind of function will not depend on any of the instances or class variables.
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
        """
        returns the total number of employee objects already created
        """
        return cls.num_of_emps
    
    @staticmethod
    def is_workday(day):
        """
        Takes in a date, converts it to a day of the week (integer), and returns 
        whether or not it is a workday (weekday).
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('John', 'Smith', 60000)

import datetime

my_date = datetime.date(2021, 5, 29)

print(Employee.is_workday(my_date))
