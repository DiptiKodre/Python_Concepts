# def genrators():
#     for i in range(1,5):
#         yield i

# g = genrators()
# print(next(g))

# for i in g:
#     print(i)

# def count():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# for i in count():
#     print(i)

def fruits():
    yield "Mango"
    yield "Banana"
    yield "Grapes"
    yield "Apple"
gen = fruits()
for i in gen:
    print(i)
#print(next(fruits()))


# #generator comprehension
# square = (x*x for x in range(1,6))
# for i in square:
#     print(i)


    