# STRING FORMATTING

userName = input("name: ")
greetName = "welcome {}".format(userName)

print(greetName)

# another string format
userInputName = input("nickname: ")
messageName = f"Hello {userInputName}"

print(messageName)

# multiple string format
firstname = input("given name: ")
lastname = input("lastname: ")
age = int(input("age: "))

personInfo = "name: {} lastname: {} age: {}".format(firstname, lastname, age)

print(personInfo)