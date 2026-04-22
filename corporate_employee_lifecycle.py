import gc
import sys

class Company:

    class Employee:
        def __init__(self, company, emp_id, name):
            self.company = company
            self.emp_id = emp_id
            self.name = name

        def display(self):
            print(self.emp_id, self.name, "-", self.company.cname)

    def __init__(self, cname):
        self.cname = cname
        self.employees = []

    def add_employee(self, emp_id, name):
        emp = Company.Employee(self, emp_id, name)
        self.employees.append(emp)
        print("Reference Count:", sys.getrefcount(emp))

    def remove_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                del emp
                gc.collect()
                print("Employee removed")
                return

    def display_all(self):
        for emp in self.employees:
            emp.display()


cname = input("Enter company name: ")
c = Company(cname)

n = int(input("Enter number of employees: "))
for _ in range(n):
    eid = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    c.add_employee(eid, name)

c.display_all()

rid = input("Enter employee ID to remove: ")
c.remove_employee(rid)

print("Remaining Employees:")
c.display_all()

gc.collect()
