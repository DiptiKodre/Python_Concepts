#Enumerate() --> used when we want to loop through a sequence  and get both index and value
#syntax : enumerate(iterable, start=0)
#built in function that adds a counter to an iterable and returns pairs of (index, value)

names = ["dipti","neha","nikita"]
for i,name in enumerate(names):
    print(i, name)


#This code converts the enumerate object into a list of tuples. 
# Each tuple contains the index and corresponding element from the list.
alphabets = ["a","b","c","d"]
res = enumerate(alphabets)
print(list(res))  # Output: [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

# This code retrieves elements one by one using next() on enumerate object.

aplhab = ["x","y","z"]
result = enumerate(aplhab)
print(next(result))  # Output: (0, 'x')
print(next(result))  # Output: (1, 'y')

# This code enumerates dictionary items and provides index with key-value pairs.
dict = {"name":"neha","age":23,"city":"pune"}
for idx,(key, value) in enumerate(dict.items()):
    print(idx, key, value)