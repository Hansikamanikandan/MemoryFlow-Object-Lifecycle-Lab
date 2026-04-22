import gc

class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def display(self):
        print("City:", self.city)
        print("State:", self.state)

    def __del__(self):
        print("Address object garbage collected")


class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
        self.address = None

    def add_address(self):
        city = input("Enter City: ")
        state = input("Enter State: ")
        self.address = Address(city, state)

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        if self.address:
            self.address.display()

    def resign(self):
        print(self.name, "has resigned")
        self.address = None


employees = []
n = int(input("Enter number of employees: "))

for _ in range(n):
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    e = Employee(emp_id, name)
    e.add_address()
    employees.append(e)

for e in employees:
    e.display()

rid = int(input("Enter Employee ID who resigned: "))
for e in employees:
    if e.emp_id == rid:
        e.resign()
        employees.remove(e)
        del e
        break

gc.collect()
