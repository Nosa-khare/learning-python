
# Parent class
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


"""
To enable the subclass instantiate with more data than the parent class
 can take, (i.e to add more parameters to the __init__()). The subclass
 should be given its own __init__() method
"""


# noinspection SpellCheckingInspection
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)  # Allows the parent class
        # init method to handle the arguments specified
        self.pro_lang = prog_lang  # subclass init method handles this argument


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('John', 'Smith', 60000, 'Java')

print(dev_2.fullname())
print(dev_1.pro_lang)
