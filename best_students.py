class Student:
  def __init__(self, firstName, lastName, id, average):
    self.firstName = firstName
    self.lastName = lastName
    self.id = id
    self.average = average

student1 = Student('Jack', 'Sparrow', 1, 92)
student2 = Student('Hector', 'Barbosa', 2, 82)
student3 = Student('Frank', 'Castle', 3, 84)
student4 = Student('Bruce', 'Wayne', 4, 99)
student5 = Student('Tony', 'Stark', 5, 89)
student6 = Student('Peter', 'Parker', 6, 79)

students = [student1, student2, student3, student4, student5, student6]

best_students = filter(lambda s: s.average > 90, students)
print(best_students)