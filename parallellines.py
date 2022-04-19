class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Line:
  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2

  def isParallel(self, l2):
    slope1 = (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
    slope2 = (l2.p1.y - l2.p2.y) / (l2.p1.x - l2.p2.x)
    return slope1 == slope2

l1 = Line(Point(1, 3), Point(3, 6))
l2 = Line(Point(3, 9), Point(9, 18))

print(l1.isParallel(l2))