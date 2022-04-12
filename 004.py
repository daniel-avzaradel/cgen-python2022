## 12/04/2022 - 4th meeting

# the zip() function

ids = [12, 23, 34, 14, 16]
names = ['moshe', 'daniel', 'laura', 'paola']
data = zip(ids, names)

print(type(data))

for item in data:
    print(item)


# the main() function


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