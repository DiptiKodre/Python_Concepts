class Animal:
    def __init__(self):
        print("Animal Constructor called")

class Dog(Animal):
    
          def __init__(self):
            super().__init__()  # Call the constructor of the parent class
            print("Dog Constructor called")

d1 = Dog()