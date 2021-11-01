from classes_10 import *

if __name__ == "__main__":
    
    print(isinstance(manager_1, Manager))  # True

    print(isinstance(manager_1, Employee))   # True

    print(isinstance(manager_1, Developer))  # False

    print(issubclass(Developer, Employee))  # True

    print(issubclass(Manager, Employee))  # True

    print(issubclass(Manager, Developer))  # False
