"""
Python Functions
A function is a block of code which only runs when it is called.
"""

def sum_of_num(num_1, num_2)->float:
    return num_1 + num_2

sum = sum_of_num(10,20)

print("Sum of two numbers is",sum)


def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(check_even(10))