"""
The fix is that the property decorator allows the method to be accessed like an attribute
"""


class Employee:
    num_of_emps = 0
    raise_amount = 1.04  # 4% increase

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@email.com'


    def fullname(self):
        return f'{self.first_name} {self.last_name}'


emp_1 = Employee('Corey', 'Schafer', 50000)

emp_1.first_name = "John"
print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname())

emp_1.first_name = "James"
print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname())
