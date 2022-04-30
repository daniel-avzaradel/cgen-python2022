f = lambda a, b=10: a * b
print(f(2))

## tuple packing
# built-in function len() = length
f = lambda *numbers: len(numbers)
print(f(2, 3, 4, 11, 6))

## exercise
total = lambda num1, num2: num1 + num2
print(total(8, 2))