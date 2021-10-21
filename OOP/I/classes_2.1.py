# class variables and methods
"""
--Class variables are variables shared among all instances of a class
"""


class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    
    def apply_raise(self):
        self.pay = self.pay * 1.04


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('John', 'Smith', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


"""
We see the the emp_1 pay increase by 4% after calling the apply raise method on it

However, having the raise amount hard coded into the apply raise method is bad
practice because
    *It cannot be accessed without having to come into the code directly to view 
     its value. Because it is not assigned to any variable for storage
    *It would difficult to update the value, especially if we have it referenced at different
     parts  of the code.
    *It also makes it impossible to have a different raise value for different instances (employees)
"""