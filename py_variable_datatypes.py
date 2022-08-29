# VARIABLE & DATATYPES

# variable
firstName = "rom" # string datatype
lastName = "pilapil"
fullName = firstName.title()+" "+lastName.title() # string concatenation and capitalize first letter
quantity = 2 # integer datatype
price = 123.32 # float datatype


totalPay = quantity * price # product of two variable

# output
print("user: "+firstName.upper()) # print text in uppercase
print(fullName+" total payment: ", totalPay)
print()

# datatype function
print(type(firstName), firstName)
print(type(quantity), quantity)
print(type(price), price)