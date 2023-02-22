"""Module to perform arithmetic calculations"""


def add_numbers(*nums):
    """add a series of numbers"""
    try:
        result = 0
        for i in nums:
            result += i
        return result
    except TypeError:
        print("You have not supplied the correct argument types")
        raise


def subtract_from_num(num, num_to_subtract):
    """subtract num_to_subtract from num"""
    try:
        result = 0
        result = num - num_to_subtract
        return result if result > 0 else 0
    except TypeError:
        print("You have not supplied the correct argument types")
        raise


def multiply_two_numbers(num_one, num_two):
    """return num_one multiplied by num_two"""
    try:
        return num_one * num_two
    except TypeError:
        print("You have not supplied the correct argument types")
        raise
