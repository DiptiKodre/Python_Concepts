# Map, Filter and Reduce in Python

#map() --> applies to every element(change every element)
#keeps the same number of elements as input, just transforms them

#filter() --> filters out elements based on a condition
#keeps only the elements that satisfy the condition, may reduce the number of elements

#reduce() --> repeatedly combines elements into a single result
# from functools import reduce

#map --> modify
#filter --> select
#reduce --> combine

#use them in combination to perform complex operations on data

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

map_result = list(map(lambda x : x*2, numbers))
print("Map Result:", map_result)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

filter_result = list(filter(lambda x: x%2==0, numbers))
print("Filter Result:", filter_result)  # Output: [2, 4, 6, 8, 10]

import functools
reduce_result = functools.reduce(lambda x,y : x*y, numbers)
print("Reduce Result:", reduce_result)  # Output: 3628800

#sum of squares of even numbers

e = list(filter(lambda x :x%2 ==0, numbers))  #filtering even numbers
s = list(map(lambda x : x**2,e))     #mapping to square the even numbers
sum = functools.reduce(lambda x,y :x+y, s)  #reducing the squares to get the sum

print("Sum of squares of even numbers:", sum)  # Output: 220


#product of positive numbers
num = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positive_numbers = list(filter(lambda x :x>0, num))  #filtering positive numbers
product = functools.reduce(lambda x,y :x*y, positive_numbers) #reducing the positive numbers to get the product
print("Product of positive numbers:", product)  # Output: 10395000

prod = functools.reduce(lambda x,y : x*y,filter(lambda x :x>0,num))  #filtering positive numbers and reducing to get the product
print("Product of positive numbers:", prod)  # Output: 10395000


#sum of lengths of words containing vowels
words = ["hello", "world", "python", "programming", "is", "awesome"]
vowels_words = list((filter(lambda x:any(c in 'aeiou' for c in x), words)))  #filtering words containing vowels
lengths = list(map(lambda x: len(x), vowels_words))  #mapping to get the lengths of the words containing vowels
sum = functools.reduce(lambda x,y : x+y, lengths)  #reducing the lengths to get the sum
print("Sum of lengths of words containing vowels:", sum)  # Output: 28