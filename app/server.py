'''Server code'''

import calculator


def print_hello_world():
    '''Prints a hello world message'''
    print("hello world!")


print(calculator.add_numbers("brian", "Ahern"))
print(calculator.add_numbers(9, 8, 7, 6, 5, 4, 3, 2, 1))

print(calculator.multiply_two_numbers(5, 5))

print_hello_world()
