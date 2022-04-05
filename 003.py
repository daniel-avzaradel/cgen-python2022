# Functions

def f(numbers):
    numbers[0] = 99

ob = [12, 4, 76]

f(ob)
print(ob)

sales = 5000
income = 1000

if sales>1000:
    def bonus(income):
        return income * 0.1
else:
    income *= 0.05

print(income)

# nonlocal
# defines a variable not to be on local scope

## nested functions

def a():
    temp = 12
    def b():
        nonlocal temp
        temp = 4
    b()
    print(temp)
    return temp
a()

def doSomething():
    global temp
    temp = 99
    print(temp)

doSomething()

# the func(name=value) syntax

def f(a, b):
    print(a, b)

x = f(a=3, b=5)

## unpacking values

def total(*tpl):
    sum = 0
    for x in tpl:
        sum = sum + x
    return sum

print(total(1, 4, 6, 12, 22))
