f = lambda a, b=10: a * b
print(f(2))

## tuple packing
# built-in function len() = length
f = lambda *numbers: len(numbers)
print(f(2, 3, 4, 11, 6))

## exercise
total = lambda num1, num2: num1 + num2
print(total(8, 2))


# High Order Functions
def convert(items: list, f: callable):
  result: list = list()
  for item in items:
    result.append(f(item))
  return result

def f(num):
  return num * 10

numbers1 = [10, 2, 4]

print(convert(numbers1, f))