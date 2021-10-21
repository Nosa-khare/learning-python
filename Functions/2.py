
""" function that takes positional only /required argument """


def hello_function(greeting, /):
    return f'{greeting} function.'


# called with a corresponding positional argument
print(hello_function('Hi'))
# print(hello_function())  # throws error


""" function that takes positional only / optional arguments """


def hello(greeting='Hi', name='you!', /):
    return f'{greeting}, {name}'


print(hello())
print(hello('you', 'Hi'))
# print(hello(name='you', greeting='Hi')) # Throws and error


""" function that takes positional or keyword / optional arguments """


def hello(greeting='Hi', name='you!'):
    return f'{greeting}, {name}'


print(hello())
print(hello('you', 'Hi'))
print(hello(name='you', greeting='Hi'))


""" function that takes keyword only / required arguments """


def hello(*, greeting, name):
    return f'{greeting}, {name}'


print(hello(name='you', greeting='Hi'))
# print(hello('you', 'Hi'))  # Throws error
# print(hello())  # Throws error


""" function that takes keyword only / optional arguments """


def hello(*, greeting='Hi', name='you!'):
    return f'{greeting}, {name}'


print(hello())
print(hello(name='you', greeting='Hi'))
