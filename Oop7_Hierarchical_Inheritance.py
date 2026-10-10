class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

class Cat(Animal):
    def meow(self):
        print("Meowing...")

d1 = Dog()
d1.eat()  # Inherited method from Animal class
d1.bark()  # Method from Dog class

c1 = Cat()
c1.eat()  # Inherited method from Animal class
c1.meow()  # Method from Cat class