# Dictionaries
# Dictionaries a kind of Hash-Table Type and work like AssoCiatives Arrays found
# in JavaScript. Dictionary consist of Key Value Pairs.
# A Key can be any Data Type that Associates with the Value.


adict = {}                  # An Empty Dictionary

numdict = {                 # A Number Dictionary
    'one': 1,
    'two': 2,
    'three': 3
}

strdict = {                 # A String Dictionary
    1: 'Victor',
    2: 'Absalom',
    3: 'Arnold',
    4: 'Zuriel',
    5: 'Ezekiel'
}

mixdict = {                 # A Mix Dictionary
    123: 'Some String',
    '456': 456
}

# Diplaying Dictionaries
print(adict)
print(numdict)
print(strdict)
print(mixdict)

input()

# Access Values Using Keys
print(numdict['two'])
print(strdict[5])
print(mixdict['456'])

input()

# Adding Value to Dictionary
adict[0] = 'First Index'
numdict['four'] = 4
strdict[6] = 'Unknown'

print(adict)
print(numdict)
print(strdict)
