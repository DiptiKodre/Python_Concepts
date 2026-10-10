class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def hobbies(self):
        print("Cooking, Art")

class Child(Father,Mother):
    def likes(self):
        print("Sports, Music")

c1 = Child()
c1.hobbies()  # Inherited method from Mother class
c1.skills()  # Inherited method from Father class
c1.likes()   # Method from Child class