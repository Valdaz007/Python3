# Tuples
# A Tuple consists of items seperated by a Comma (,) enclosed in Parenthesis (()).
# The Main Difference between Tuples and Lists is that Lists are Mutable meaning 
# the Size and Values can be Changed while Tuples Cannnot thus they are Immutable.

atuple = ()                                     # An Empty ValueTuple
numtuple = (100, 200, 300, 450)                 # A Integer Value Tuple
strtuple = ('Victor', 'Volsavai', '20161232')   # A String Value Tuple
mixtuple = ('abcd', 789, 'john', 70.2)          # A Mixed Value Tuple

print(atuple)
print(numtuple)
print(strtuple)
print(mixtuple)

input()

# Accessing Tuple Index
print(numtuple[3])
print(strtuple[0])
print(mixtuple[1])