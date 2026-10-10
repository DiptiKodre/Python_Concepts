class Employee:
    def __init__(self, name,age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print("Name : ", self.name, "Age : ", self.age, "Salary : ", self.salary)

s1 = Employee("Dipti", 24, 22000)
s1.display()