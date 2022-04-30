f = lambda a, b=10: a * b
print(f(2))

## tuple packing

f = lambda *numbers: len(numbers)
print(f(2, 3, 4, 11, 6))