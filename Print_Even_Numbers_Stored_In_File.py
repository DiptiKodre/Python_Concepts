count = 0
with open("numbers.txt", "r") as f:
    data = f.read()
    print(data)

    # num = " "
    # for i in range(len(data)):
    #     if data[i] == ",":
    #         if int(num) % 2 == 0:
    #             count += 1
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]  
    # if num:
    #     print(int(num))
    # if int(num) % 2 == 0:
    #     count += 1
    # print("Total even numbers in file are: ", count)
     

    nums = data.split(",")
    for val in nums:
        if int(val) % 2 == 0:
            count += 1
    print("Total even numbers in file are: ", count)
    



