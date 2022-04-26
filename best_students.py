class Student:
  def __init__(self, firstName, lastName, id, average):
    self.firstName = firstName
    self.lastName = lastName
    self.id = id
    self.average = average
  def __str__(self) -> str:
      return '%s %s' % (self.firstName, self.lastName)


students = [Student('Jack', 'Sparrow', 1, 92), Student('Hector', 'Barbosa', 2, 82), Student('Frank', 'Castle', 3, 84), Student('Bruce', 'Wayne', 4, 99), Student('Tony', 'Stark', 5, 89), Student('Peter', 'Parker', 6, 79)
]

x = filter(lambda s: s.average > 90, students)

for ob in x:
  print(ob)