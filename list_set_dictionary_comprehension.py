numbers = [12,23,11,14,16,17]

#list comprehension

square = [x*x for x in numbers]
print(square)
print(type(square))

#with condition
even_square = [x*x for x in numbers if x%2==0]
print(even_square)

table =[10*i for i in range(1,11)]
print(table)

#dictionary comprehension
dict_square = {x:x*x for x in numbers}
print(dict_square)
print(type(dict_square))

state = ["Maharashtra","Gujarat","Rajasthan","Madhya Pradesh"]
capital = ["Mumbai","Gandhinagar","Jaipur","Bhopal"]
dict_state_capital = {s:c for s,c in zip(state,capital)}
print(dict_state_capital)

#with condition
dict_cube ={x:x*x*x for x in numbers if x%2==0}
print(dict_cube)

#set comprehension
set_square = {x*x for x in numbers}
print(set_square)
print(type(set_square))

set_multiply = {x*5 for x in range(1,11)}
print(set_multiply)

num = [1,2,1,2,3,4,5,6,7,8,9,10]
set_unique = {x for x in num}
print(set_unique)

#with condition
set_cube = {x*x*x for x in numbers if x%2==0}
print(set_cube)


#generator comprehension
gen_square = (x*x for x in numbers)
print(gen_square)
print(type(gen_square))
for i in gen_square:
    print(i)

#with condition
gen_cube = (x*x*x for x in numbers if x%2==0)
for i in gen_cube:
    print(i)    



