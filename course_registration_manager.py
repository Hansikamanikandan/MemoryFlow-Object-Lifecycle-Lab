import sys

class Course:
    def __init__(self, name):
        self.course_name = name

    def display(self):
        print("Course:", self.course_name)


class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.courses = []

    def register_course(self):
        cname = input("Enter course name: ")
        c = Course(cname)
        self.courses.append(c)
        print("Reference Count:", sys.getrefcount(c))

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Enrolled Courses:")
        for c in self.courses:
            c.display()


roll_no = int(input("Enter roll no: "))
name = input("Enter student name: ")
s = Student(roll_no, name)

n = int(input("Enter number of courses: "))
for _ in range(n):
    s.register_course()

s.display()
