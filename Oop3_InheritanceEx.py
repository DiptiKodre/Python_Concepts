class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

d1 = Dog()
d1.eat()  # Inherited method from Animal class
d1.bark()  # Method from Dog class