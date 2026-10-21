def SearchInFile():
    word = input("Enter a word to search in file: ")
    with open("sample.txt","r") as f:
        data = f.read()
        if word in data:
            print("The word is present in the file")
        else:
            print("The word is not present in the file")

SearchInFile()   