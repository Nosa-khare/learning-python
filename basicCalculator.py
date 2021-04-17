import re
from textwrap import dedent

run = True
previous_result = 0


def solve_equation():

    """this function performs all calculations
        it uses the regex.sub to remove non mathematical
        characters
        """

    global run
    global previous_result

    if previous_result == 0:
        equation = input("\nEnter equation: ")
    else:
        equation = input(str(previous_result))

    if equation.lower() == 'quit':
        print("Goodbye!")
        run = False
    elif equation.lower() == 'clear':
        previous_result = 0
    else:
        equation = re.sub('[a-zA-Z,()@$&_~`?;\'|{}:" "]', "", equation)
        if previous_result == 0:
            previous_result = (eval(equation))
        else:
            previous_result = eval(str(previous_result) + equation)


# Program Starts
print(dedent("""
            Basic Calculator!
            Type clear to refresh
            Type 'quit' to exit calculator"""))

while run:
    solve_equation()
