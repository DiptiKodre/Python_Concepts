#Positional arguments and keyword arguments

def add(*args):
    print(args)
    return(sum(args))
print(add(10,20,30))
print(add(23,34,45,56,67))

def student(**kwargs):
    print(kwargs)
student(name = "dipti", age=24,city="Pune")


def details(*args, **kwargs):
    print("Args: " , args)
    print("Kwargs : " ,kwargs)
details(10,20,30,40, name="dipti",city="Pune")

def greet(*numbers, **details):
    print("Numbers: ",numbers)
    print("Details: ",details)  
greet(10,20,30,40, name="dipti",city="Pune")

def greet(name, *args,**kwargs):
    print("Name: ",name)
    print("Args: ",args)
    print("Kwargs: ",kwargs)
greet("dipti",10,20,30,40, city="Pune",state="Maharashtra")

def info(*args):
    for i in args:
        print(i)
info("pune","mumbai","nagpur","nashik")

def capitals(**kwargs):
    for key,value in kwargs.items():
        print(key," : ", value)
capitals(Maharashtra="Mumbai", Madhya_Pradesh="Bhopal", Rajasthan="Jaipur", Gujarat="Gandhinagar", Karnataka ="Banglore")
