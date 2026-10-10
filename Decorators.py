def decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper

@decorator
def greet():
    print("Hello...!!")

greet()

# example of decorator with arguments
def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div)
div(2,4)


#decorator with arguments using @ symbol
def decorator(func):
    def wrapper(*args,**kwargs):
        print("Function is starting...")
        result = func(*args,**kwargs)
        print("Function has ended...")
        return result
    return wrapper

@decorator
def add(a,b):   
    return a+b
print(add(100,200))
