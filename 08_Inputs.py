# Inputs
# A more Realistic Approach to Programming is taking users Inputs
# and Manupilating it.

# The 'input()' Method is an In-Built Method that allows us to take
# users inputs.
# The Method takes in between its Perenthesis () an Optional String
# Argument as Prompt for User Input.

# Note that the method Only Returns a String Data Type of the
# Users Input whatever the Input may be.


# Takes the Input from User and Prints it out.
print(f'{input()}\n')      


# Prompt for User Input and Prints it out.
print(f'{input("Type Something: ")}\n')


# Storing User Input and Prints it out.
str_input = input("Type Something to Store: ")
print(f'{str_input}\n')


# Simple Calculator
print('Simple Calculator')
num1 = input('Type in a the First Number: ')
num2 = input('Type in a the Second Number: ')

print(f'num1 + num2 = {num1 + num2}\n')

# What's Wrong with our Simple Calculator???
# The Input Method only Returns String Data Type

# Simple Calculator 2.0
print('Simple Calculator 2.0')
num1 = int(input('Type in a the First Number: '))
num2 = int(input('Type in a the Second Number: '))

print(f'num1 + num2 = {num1 + num2}\n')

