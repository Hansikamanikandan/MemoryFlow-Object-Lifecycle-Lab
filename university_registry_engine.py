import gc
import sys

class University:
    def __init__(self, name):
        self.university_name = name
        self.students = []

    class Student:
        def __init__(self, rollno, name, university):
            self.rollno = rollno
            self.name = name
            self.university = university

        def display_details(self):
            print("Roll No:", self.rollno)
            print("Name:", self.name)
            print("University:", self.university.university_name)

        def __del__(self):
            print("Student object deleted")

    def add_student(self):
        r = int(input("Enter Roll No: "))
        n = input("Enter Name: ")
        s = University.Student(r, n, self)
        print("Reference Count:", sys.getrefcount(s))
        self.students.append(s)

    def remove_student(self):
        r = int(input("Enter Roll No to remove: "))
        for s in self.students:
            if s.rollno == r:
                self.students.remove(s)
                del s
                print("Student Removed")
                return

    def display_all(self):
        for s in self.students:
            s.display_details()


gc.enable()
u_name = input("Enter University Name: ")
u = University(u_name)

n = int(input("Enter number of students: "))
for _ in range(n):
    u.add_student()

u.display_all()
u.remove_student()
gc.collect()
