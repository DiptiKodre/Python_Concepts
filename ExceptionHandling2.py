def fun():
    try:
        list = [1,4,5,7]
        idx = int(input("Enter the index: "))
        print(list(idx))
        return 1
    except:
        print("Some error occurred")
        return 0

    finally:
        print("I'm always executed")

print(fun())