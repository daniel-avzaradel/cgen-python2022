
def calculate(num1, num2):
    result = num1
    r = range(num1, (num2+1))

    for x in r:
        print('x =', x)
        if num1 == num2:
            result = num1*num2
            break
        if x == num1: continue
        result *= x
        print(result)
    
    print(result)
    return result

calculate(3, 4)

def factorial(num):
    fact = num
    while num > 1:
        fact = fact * (num-1)
        num -= 1

    print(fact)
    return fact

factorial(6)

def multiply(numbers):
    result = 1

    for n in numbers:
        result *= n
    
    print(result)
    return result

multiply([2, 4, 10, 2])

# a = 3
# b = 4
# print("hello" if b>a else "salam")
# print('haifa' if b>a and b>0 else 'ramat-gan')
# print(109 if a>b else 'rehovot')
# print('tel-aviv' if 'a' in ['a','b','c','d'] else 'rehovot')
# print('tel-aviv' if 'a' in 'abcd' else 'rehovot')
# print('blue' if 'b' not in "mosh" else 'red')
# print('winter' if a>2 and a%2==1 else "summer")
# print(123 if 'y' not in 'yahoo' else 'x')
