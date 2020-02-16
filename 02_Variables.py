# Lists
# A List contain items seperated by Commas (,) and are enclosed within Brackets ([]).
# List is similar to Arrays in C and C++ but can contain different data types.

# Creating a List:
alist = []                                  # An Empty List
numlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    # A List Containing Numbers
strlist = ['Hello', 'World']                # A List Containing Texts / Strings
mixlist = ['Victor', 25, 'Male', 20161232]  # A List Containing Mix Data Types

print(alist)
print(numlist)
print(strlist)
print(mixlist)

input() # Wait for a Keyboard Event to Continue

# Accessing List Index
print(numlist[1])
print(strlist[1])

input() # Wait for a Keyboard Event

# Adding Items to List using In-Built List Method 'append()'
alist.append('First')
numlist.append(10)
strlist.append('Victor')
mixlist.append('23-10-94')

print(alist)
print(numlist)
print(strlist)
print(mixlist)

input() # Wait for a Keyboard Event

#Removing Items From a List using In-Built List Method 'pop()'
alist.pop()
numlist.pop(0)
strlist.pop(1)
mixlist.pop()

print(alist)
print(numlist)
print(strlist)
print(mixlist)
