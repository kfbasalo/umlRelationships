# Class 1
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)


# Class 2
class School:
    def __init__(self, student):
        self.student = student

    def show_student(self):
        self.student.display()


# Main Program
s1 = Student("Kirby")
school = School(s1)

school.show_student()
