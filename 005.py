## Classes

class myClass:
  def setData(self, value):
      self.name = value
  def printName(self):
    print(self.name)

john = myClass()
john.setData('John')
john.printName()

## the simplest python class definition

class myNewClass: pass
ob = myNewClass()
ob.text = 'abc'
ob.numbers = 123
print(ob.text, ob.numbers)


## the __init__ function
## The __init__ method is Python's replacement for the constructor. When we create a new object this function will be invoked. 

class Rectangle:
  def __init__(self, w, h):
    self.width = w
    self.height = h
  def printDetails(self):
    print('width:', self.width, 'height:', self.height)
  def area(self):
    print('the area of the rectangle is:', self.width * self.height)

newRectangle = Rectangle(12, 20)
newRectangle.printDetails()
newRectangle.area()


## polymorphism in Python

class Dog:
  def __init__(self, name):
    self.name = name
  def hello(self):
    print("wof wof")

class Cat:
  def __init__(self, name):
    self.name = name
  def hello(self):
    print("miau miau")

class Cow:
  def __init__(self, name):
    self.name = name
  def hello(self):
    print("moo moo")

cow = Cow('Mitsy')
cat = Cat('Cookie')
dog = Dog('Kevin')

print(dog.name, cow.name, cat.name)


### exception handling

def func(num):
  if num < 0:
    raise IndexError
  return num * 10

try:
 num = 18-12
 print(func(num))
except:
 print('exception was caught')
print('continue...')
try:
 num = 8-12
 print(func(num))
except:
 print('exception was caught')
print('continue...')