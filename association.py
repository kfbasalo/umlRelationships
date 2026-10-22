# Class 1
class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(self.name, "is teaching")


# Class 2
class Student:
    def __init__(self, name):
        self.name = name

    def learn(self, teacher):
        print(self.name, "is learning from", teacher.name)


# Main Program
teacher = Teacher("Mr. John")
student = Student("Kirby")

teacher.teach()
student.learn(teacher)
