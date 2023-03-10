"""
Python if...elif...else Statement
The if...elif...else statement is used in Python for decision making.
"""
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

choice = input("Enter the choice + / - / * / / %: ")

if choice == "+":
    sum = num_1 + num_2
    print("Sum of two numbers is",sum)
elif choice == "-":
    diff = num_1 - num_2
    print("Difference of two numbers is",diff)
elif choice == "*":
    product = num_1 * num_2
    print("Product of two numbers is",product)
elif choice == "/":
    quotient = num_1 / num_2
    print("Quotient of two numbers is",quotient)
elif choice == "%":
    remainder = num_1 % num_2
    print("Remainder of two numbers is",remainder)
else:
    print("Invalid choice")

# Output:
"""

Enter first number: 40
Enter second number: 10
Enter the choice + / - / * / / %: *
Product of two numbers is 400.0

"""