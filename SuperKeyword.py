#super() is a built in function used to access methods and constructors
#from parent or next class in MRO(Method Resolution Order).
#It is commonly used in inheritance to reuse parent-class functionality
# and avoid directly refferring to the pareny class name

#super for calling parent 

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")
        super().sound()

d1 = Dog()
d1.sound()

#calling parent constructor

class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Construtor")
        
c1 = Child()

#Passing Arguments to the parent Constructor

class Person:
    def __init__(self,name):
        self.name = name

class Employee(Person):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary = salary
e1 = Employee("dipti",22000)
print(e1.name)
print(e1.salary)

#super() with multiple inheritance

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")
class C(B):
    def show(self):
        super().show()
        print("C")

c = C()
c.show()

