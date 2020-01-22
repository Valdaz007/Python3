# Loops
# Loops allows for Executing BLock of Codes several times.
# Given a Conditions a Statement can be Executed multiple times if satisfied. 


# Program to Print Hello, World 3x


print("While Loop")
# While Loop
count = 3
while count > 0:
    print(f"{count}. Hello, World")
    count -= 1


input('\nPress Enter to Continue!\n')


print("For Loop")
# For Loops
for i in range(3):
    print(f"{i}. Hello, World")