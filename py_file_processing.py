# FILE PROCESSING

# read file
#fileRead = open("fruits.txt")
#readContent = fileRead.read() # cursor

#print(readContent)

#fileRead.close() # closing file

# using with
#with open("fruits.txt") as readFile:
#    content = readFile.read()
    
#print(content)

# write file
#with open("vegetables.txt", "a+") as writeFile:
#    writeFile.write("Tomato\nCucumber\nOnion\n")
#    writeFile.write("Garlic")

# append text in file
with open("vegetables.txt", "a+") as appenReadFile:
    appenReadFile.write("\nCarrot")
    appenReadFile.seek(0)
    content = appenReadFile.read()

print(content)
