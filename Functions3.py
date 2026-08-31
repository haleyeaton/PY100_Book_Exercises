def multiply(left , right):
    return left * right

def get_number(prompt):
    entry = input(prompt)
    return float(entry)

first_number = get_number('Enter the first number: ')
second_number = get_number('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Global:	multiply, get_num, first_number, second_number, product
    # Functions defined in a program file are global, unless
    # defined as an object property or nested in another function.
# Local:	left, right, prompt
    # Function parameters and variables initialized inside a function
# Built-in:     float, input, print

#  multiply, get_num, input, float, and print are function names
# left and right, and prompt are parameters. the rest of the ( ) are arguments
