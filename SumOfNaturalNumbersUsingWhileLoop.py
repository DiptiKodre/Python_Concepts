n = int(input("Enter a number to find sum of natural numbers: "))

sum = 0
i = 1
while i<=n:
    sum += i
    i += 1
print("The sum of first" ,n, "natural numbers is : ", sum)