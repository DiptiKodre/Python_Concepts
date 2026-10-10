print(5 + 10)  # Output: 15
print("Hello " + "World")  # Output: Hello World
print([1, 2] + [3, 4])  # Output: [1, 2, 3, 4]



class Student:
    def __init__(self,marks):
        self.marks = marks

    def __add__(self,other):
        return self.marks + other.marks

s1 = Student(85)
s2 = Student(90)
print(s1 + s2)  # Output: 175