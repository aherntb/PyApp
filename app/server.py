'''Server code'''

from science import calculator


def print_hello_world():
    '''Prints a hello world message'''
    print("hello world!")


print(calculator.add_numbers("brian", "Ahern"))
print(calculator.add_numbers(9, 8, 7, 6, 5, 4, 3, 2, 1))

print(calculator.multiply_two_numbers(5, 5))

print_hello_world()


class Person:
    """Person class for encapsulating a person"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_details(self):
        """Prints personal details of a Person"""
        print(
            f"Person with First Name: {self.first_name} Last Name: {self.last_name} Age: {self.age}")


p1 = Person("Brian", "Ahern", 37)

p1.print_details()
