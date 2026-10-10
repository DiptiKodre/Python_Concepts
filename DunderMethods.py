class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __str__(self):
         return f"Student({self.name}, {self.marks})"

    def __repr__(self):
           return f"Student(name={self.name!r}, marks={self.marks!r})"
        
    def __len__(self):
        return len(self.name)

    def __add__(self,other):
        return self.marks + other.marks

    def __eq__(self,other):
        return self.name==other.name and self.marks == other.marks

s1 = Student("dipti",90)
s2 = Student("dipti",90)

print(str(s1))   #__str__
print(repr(s1))  #__repr__
print(len(s1))   #__len__
print(s1+s2)     #__add__
print(s1==s2)    #__eq__