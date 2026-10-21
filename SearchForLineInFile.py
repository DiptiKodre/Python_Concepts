def SearchForLineInFile():
    data = True
    line = input("Enter a line to search in file: ")
    line_no = 1
    with open("sample.txt","r") as f:
        
        while data:
            data = f.readline()
            if (line in data):
                print(line_no)
                return
            line_no += 1

        return -1

print(SearchForLineInFile())



