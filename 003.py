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


## nested functions