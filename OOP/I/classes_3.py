
"""
- If we were to update the class attribute raise amount, it would be updated
   for the class and all its instances, but;
- If we were to update the class attribute for and instance, it would update and assign 
   the attribute fot that instance alone, while leaving the class attribute and all other 
   instances unchanged.
  In this case the updated attribute now becomes an instance variable and would be 
   seen in the instance name space 
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

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.raise_amount = 1.05
print('\nUpdate through class')
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('emp_1 name space:', emp_1.__dict__)  # still no raise_amount attr

emp_1.raise_amount = 1.10
print('\nUpdate through instance')
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('emp_1 name space:', emp_1.__dict__)  # now has raise_amount attr

"""
-This concept then show that different outcomes can be gotten depending on how
 the attribute was referenced in the class method. i.e 
    *self.variable
    *Class.variable
"""
