#python supports duck typing
#"If it looks like a duck and quacks like a duck, then it must be a duck"
#the object class does not matter, what matters is whether it has required methods and properties or not.

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()

make_sound(dog)  # Output: Dog barks
make_sound(cat)  # Output: Cat meows

#make_Sound() does not care about object is of dog or cat class.
#  it only expects the object to have sound() method