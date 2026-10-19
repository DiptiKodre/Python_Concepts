cities = ["pune", "mumbai", "delhi", "bangalore", "chennai"]    
actors = ["shahrukh", "salman", "akshay", "ajay", "ranbir"]

def list_length(list):
    return len(list)

print("Length of cities list: ", list_length(cities))
print("Length of actors list: ", list_length(actors))

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(cities)
print()
print_list(actors)
print()
