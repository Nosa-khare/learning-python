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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)  # Allows the parent class
        # init method to handle the arguments specified
        self.pro_lang = prog_lang  # subclass init method handles this argument


class Manager(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, employees=None):

        """
        Upon creating a new manager there will be the option of passing in a list
        of employees which the manager supervises
        """

        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        # The employees argument is default to None and not straight up an empty list because its
        # not best practice to set a mutable datatype as a default argument.

    def add_emp(self, emp):
        """
        Function to add an employee to the list of those managed by the manager
        """

        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        """
        Function to remove an employee from the list of those managed by the manager
        """

        if emp in self.employees:
            self.employees.remove(emp)

    def display_emps(self):

        """
        Function to print out all employees managed by the manager
        """
        for i, value in enumerate(self.employees, start=1):
            print(f'{i}. {value.fullname()}')


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('John', 'Smith', 60000, 'Java')

manager_1 = Manager('Nosakhare', 'Edokpayi', 150000, [dev_2])

if __name__ == "__main__":
    print('Manager:', manager_1.fullname())
    print('Employee list:')
    manager_1.display_emps()

    print('\nAdding employee...')
    manager_1.add_emp(dev_1)

    print('\nNew employee list:')
    manager_1.display_emps()

    print('\nRemoving employee...')
    manager_1.remove_emp(dev_2)

    print('\nNew employee list:')
    manager_1.display_emps()
