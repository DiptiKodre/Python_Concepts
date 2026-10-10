add = lambda x,y:x+y
print(add(10,20))

square = lambda x: x*x
print(square(10))

cube = lambda x: x*x*x
print(cube(3))

# Using lambda with map function
numbers = [1,2,3,4,5,6,7,8,9]
squares = list(map(lambda x : x*x,numbers))
print(squares)

#Using lambda with filter function
even = list(filter(lambda x : x%2==0, numbers))
print(even)

#Using lambda with reduce function
from functools import reduce
product = reduce(lambda x,y:x*y,numbers)
print(product)

total = reduce(lambda x,y:x+y,numbers)
print(total)

minimum = reduce(lambda x,y : x if x<y else y, numbers)
print(minimum)

maximum = reduce(lambda x,y : x if x>y else y, numbers)
print(maximum)

#Using lambda with sorted function
employees = [("dipti",24),("neha",23),("nikita",24),("priya",22),("sneha",25)]
sorted_employees = sorted(employees,key=lambda x:x[1])
print(sorted_employees)

sorted_employees = sorted(employees,key=lambda x:x[1],reverse=True)
print(sorted_employees)

sorted_employees = sorted(employees,key=lambda x:x[0])
print(sorted_employees)

#Using lambda with list comprehension
squares = [lambda x=x: x*x for x in range(10)]
for i in squares:
    print(i())

#Using lambda for conditional expressions
max_num = lambda x,y: x if x>y else y
print(max_num(10,20))

check_negative_positive = lambda x: "Positive" if x>0 else "Negative" if x<0 else "Zero"
print(check_negative_positive(10))
print(check_negative_positive(-10))
print(check_negative_positive(0))

#Return multiple results using lambda
calculate = lambda x,y: (x+y,x-y,x*y,x/y)
result = calculate(10,5)
print(result)