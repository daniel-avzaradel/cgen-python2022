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