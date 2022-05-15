## Classes

class myClass:
  def setData(self, value):
      self.name = value
  def printName(self):
    print(self.name)

john = myClass()
john.setData('John')
john.printName()