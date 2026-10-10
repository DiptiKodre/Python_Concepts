class Animal:

    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

class Puppy(Dog):
    def play(self):
        print("Playing...")

p1 = Puppy()
p1.eat()  # Inherited method from Animal class      
p1.bark()  # Inherited method from Dog class
p1.play()  # Method from Puppy class        