"""
Class methods can be used as alternative constructors. i.e. to provide
 multiple ways to create objects.

For example, when the employee data needed to instantiate a new employee object
 is been retrieved in form of a string, separated by hyphens, and is having to 
 undergo parsing each time a new object is to be created

A class method (from_string(cls, string)) can then be created to take in these 
 strings and parse into format that can then be used to instantiate the class.
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
    
    @classmethod
    def from_string(cls, emp_string):
        """
        takes in a string as argument parses by splitting into words, unpacks the data to create new employee
        object, and then returns the object
        """
        first_name, last_name, pay = emp_string.split('-')
        return cls(first_name, last_name, pay)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('John', 'Smith', 60000)

employee_str_1 = 'John-Doe-70000'
employee_str_2 = 'Steve-Smith-30000'
employee_str_3 = 'Jane-Doe-90000'

new_employee_1 = Employee.from_string(employee_str_1)

print(new_employee_1.fullname())
