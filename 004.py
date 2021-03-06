## 12/04/2022 - 4th meeting

# the zip() function

ids = [12, 23, 34, 14, 16]
names = ['moshe', 'daniel', 'laura', 'paola']
data = zip(ids, names)

print(type(data))

for item in data:
    print(item)


# CLASSES
# Using a class statement we create a class object and assign it with a name

class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def area(self):
        return self.width * self.height

a = Rectangle(4, 3)
b = Rectangle(5, 6)

print('area of a is %d and area of b is %d' % (a.area(), b.area()))


## super()

class Person:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def details(self):
        return "id=%d name=%s" % (self.id,self.name)

class Student(Person):
    def __init__(self,id,name,average):
        self.average = average
        super().__init__(id,name)
    def details(self):
        return super().details() + " average=%d" % self.average

ob = Student(123123,"danidin",98)
print(ob.details())


## Circle

import circle

ob1 = circle.Circle(3)
ob2 = circle.Circle(6)

print(ob1.area(), ob1.perimeter())
print(ob2.area(), ob2.perimeter())