num = input("Enter a number: ")
try:
    num = int(num)
    print("You entered the number: ", num)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

except Exception as e:
    print("An error occurred:", e)