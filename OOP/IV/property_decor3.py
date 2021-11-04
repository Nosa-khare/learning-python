# Setter
# Read extensively about concept

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

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    
    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name


emp_1 = Employee('Corey', 'Schafer', 50000)

emp_1.fullname = 'Nosa Edokpayi'

print(emp_1.first_name)
print(emp_1.fullname)
