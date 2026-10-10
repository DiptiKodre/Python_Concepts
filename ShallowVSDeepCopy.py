import copy


# Shallow Copy
a = [[1,2,3],[4,5,6]]
b = copy.copy(a)
b[0][0] = 100

print(a)  # [[100, 2, 3], [4, 5, 6]]
print(b)  # [[100, 2, 3], [4, 5, 6]]

lst1 = [1, 2, 3]
lst2 = lst1.copy()
lst2[0] = 100
print(lst1)  # [1, 2, 3]
print(lst2)  # [100, 2, 3]


# Deep Copy
c = [[1,2,3],[4,5,6]]
d = copy.deepcopy(c)
d[0][0] = 100
print(c)  # [[1, 2, 3], [4, 5, 6]]
print(d)  # [[100, 2, 3], [4, 5,6]]

lst3 = [1, 2, 3]
lst4 = copy.deepcopy(lst3)
lst4[0] = 100
print(lst3)  # [1, 2, 3]
print(lst4)  # [100, 2, 3]