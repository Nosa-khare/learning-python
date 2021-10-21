# empty function
def hello_func():
    pass


result = hello_func  # stores the function object itself
result2 = hello_func()  # stores the returned value of the executed function


# print(result)
# print(result2)

# defining a function that executes a print statement
def hello():
    print('Hello function.')


# defining a function that returns a value after execution which can then be printed out
def hello_2():
    return 'Hello function.'


""" to call this function multiple times repeatedly """


# a possibility: this is wrong
print('Method 1')
exe = [print(hello_2()) for _ in range(4)]  # executes and prints the returned value of the hello_2 function 4 times,
# and then appends the returned value of the 'print' built in function each time to the exe list,
print(exe, '\n\n')  # Here you get to see that the exe list is contained by all null values.

# method: The correct way
print('Method 2')
exe = [hello_2() for _ in range(4)]  # executes the function 4 times and appends the returned value to the exe list.

for i, e in enumerate(exe):  # we can now print out as a text list
    print(e)
    if i == 3:
        print(f'Last function call returns: {e}\n')  # we know this because the last function call was the fourth
        # item appended to the list

print(exe, '\n')  # or we print exe as a python list


# Explore other formatting possibilities
exe = [hello_2() for _ in range(4)]  # executes the function 4 times and appends the returned value to the exe list.

for i, e in enumerate(exe):
    print(f'position and value: {i}, {e}')
    print('Value only:', e, '\n')
    if i == 1:
        print(f'Second function call returns: {e}\n')
