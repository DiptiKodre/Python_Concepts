def multiplier(x):

    def multiply(y):
        return x*y
    return multiply

double = multiplier(2)
triple = multiplier(3)
print(double(5))  # Output: 10
print(triple(5))  # Output: 15


#############################################################


def outer():
    message = "Hello"

    def inner():
        print(message)
    return inner

func = outer()
func()  # Output: Hello

##############################################################

def parent(name, coins):

    def play_game():
        nonlocal coins
        coins -= 1

        if coins>1:
            print(f"{name} has {coins} coins left.")
        elif coins == 1:
            print(f"{name} has {coins} coin left.")
        else:
            print(f"{name} has no coins left.")

    return play_game

neha = parent("Neha", 3)
neha()  # Output: Neha has 2 coins left.
neha()  # Output: Neha has 1 coin left.
neha()  # Output: Neha has no coins left.

nikita = parent("Nikita", 2)
nikita()  # Output: Nikita has 1 coin left.


################################################################

def outer_function(x):
    # Outer function: takes 'x' and defines inner_function
    def inner_function(y):
        return x + y  # 'x' is remembered from outer_function
    return inner_function  # Returns inner function (closure)

# Create a closure with x = 10
closure = outer_function(10)

# Call the closure with different values of 'y'
print(closure(5)) 
print(closure(20))