# The zip() function in Python is used to combine two or more
#  iterables (like lists, tuples, strings, dictionaries, etc.) into a single iterator 
# of tuples.

fruits = ["apple", "banana", "cherry"]
prices = [280, 70, 150]
zipped = list(zip(fruits, prices))
print(zipped)


# Iterables of different Lengths
# When the iterables passed to zip() have unequal lengths, 
# Python stops pairing as soon as the shortest iterable runs out of elements. 
# This ensures that zip() never tries to access a missing value from a longer iterable.
a = [1, 2, 3]
b = ['a', 'b', 'c','d']
res1 = list(zip())   #no iterable is passed to zip() function
print(res1)  # Output: []

res2 = list(zip(a))   #only one iterable is passed to zip() function
print(res2)  # Output: [(1,), (2,), (3,)]

res3 = list(zip(a, b))   #two iterables are passed to zip() function
print(res3)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


# Combine Dictionary keys and values
# zip() can also be used to pair dictionary keys and values. 
# This is useful for converting a dictionary into a list of key-value tuples
#  or when iterating over both parts together.

dict = {"name":"neha", "age": 23, "city": "pune"}
keys = dict.keys()
values = dict.values()
zipped_dict = list(zip(keys,values))
print(zipped_dict)  # Output: [('name', 'neha'), ('age', 23), ('city', 'pune')]