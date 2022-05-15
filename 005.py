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