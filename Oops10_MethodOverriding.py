#Method Overriding --> Child class provides its own implementation
#of a method defined in parent class
class Animal:
    def sound(self):
        print("Animal makes sound")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

c = Cat()
d = Dog()
c.sound()  
d.sound()