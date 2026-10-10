class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

class Cat(Animal):
    def meow(self):
        print("Meowing...")

class Hybrid(Dog, Cat):
    def play(self):
        print("Playing...")

h1 = Hybrid()
h1.eat()  # Inherited method from Animal class
h1.bark()  # Inherited method from Dog class
h1.meow()  # Inherited method from Cat class
h1.play()  # Method from Hybrid class