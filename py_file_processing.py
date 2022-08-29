# FILE PROCESSING

# read file
def readText():
    fileRead = open("fruits.txt")
    readContent = fileRead.read() # cursor
    print(readContent)
    
    fileRead.close() # closing file

readText()




# using with
def readWithFunction():
    with open("vegetables.txt") as readFile:
        readContent = readFile.read()
    
    print(readContent)

readWithFunction()

# write file
def writeText():
    with open("vegetables.txt", "w") as writeFile:
        writeFile.write("Tomato\nCucumber\nOnion\n")
        writeFile.write("Garlic")

writeText()

# append text in file
def appendText():
    with open("vegetables.txt", "a+") as appenReadFile:
        appenReadFile.write("\nCarrot")
        appenReadFile.seek(0)
        content = appenReadFile.read()
    
    print(content)
