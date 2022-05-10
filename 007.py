## Tuples
### IMMUTABLE ###

## tuple operations

()                    # creates an empty tuple
myTuple = (0,)        # creates one item tuple
myTuple = (1, 2, 3)   # creates three items tuple


## copy function

a = [1, 4, 7, 32, 20]
b = ['a', 'b', 'c', a]
print(b)

c = b.copy()
b[0] = 'abrakadabra'
print(c)

a[0] = 999
print(b)
print(c)