# X if 

# X and Y
income = 4000
temp1 = 'Israel' if income>=3000 else 'Canada'
print(temp1)

# X or Y
temp = 'gaga' or 100
print(temp)

# not X
temp = not []
print(temp)

# X in Y, X not in Y
numbers = [12, 4, 65]
for number in numbers:
    print(number)

if 12 in numbers:
    print('Yes, 12 is in numbers...')

if 88 not in numbers:
    print('88 is not in numbers')


# X is Y, X is not Y
a = [12, 3, 42]
b = [12, 3, 42]

print(a is b)
print(a == b)