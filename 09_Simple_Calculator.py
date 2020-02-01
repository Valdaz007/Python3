# This is an Exercise to Build a Simple Calculator
# using what I have already learned.

# Start

# Opening Prompt
input('Welcome to Valdaz Most Awesomest Simple Calculator\n\nPress Enter to Continue...\n')

# Loop to Continue doing Calculations
while True: # Infinit Loop
    operator = input('Enter Operator: ')
    num1 = int(input('Enter First Operand: '))
    num2 = int(input('Enter Second Operand: '))
    
    if operator == '+': print(f'{num1} + {num2} = {num1 + num2}\n')
    elif operator == '-': print(f'{num1} - {num2} = {num1 - num2}\n')
    elif operator == '*': print(f'{num1} * {num2} = {num1 * num2}\n')
    elif operator == '/': print(f'{num1} / {num2} = {num1 / num2}\n')
    elif operator == '^': print(f'{num1} ^ {num2} = {num1 ** num2}\n')

    state_input = input('Press Enter to Continue or Press Q to Exit: ')
    print()
    
    if state_input == 'Q' or state_input == 'q':
        break

print('Bye! ' * 2)

# Finish 