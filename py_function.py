# CREATING USER FUNCTION

# mean function using list
numberList = [1, 2, 3, 4, 5]

def mean(lstItem):
    meanOfList = sum(lstItem) / len(lstItem)
    
    return meanOfList

# returning with return value
print(mean(numberList)) # with variable
print(mean([1, 2, 3, 4, 5])) # manual

# curreny USD to PHP function
php = 51.36
usd = 1

def currencyConverter(peso, dollar):
    phpValue = dollar * peso
    
    print("amount in php: ", phpValue)
    return phpValue

valueInPhp = currencyConverter(php, usd) # return value place in variable

# return converted money
print(valueInPhp) # different approach
print(currencyConverter(php, usd)) # but same 
print(currencyConverter(51.36, 100))# return value
print(currencyConverter(51.36, 100)+20)

# void function return none
def converterVoid(ph,us):
    valuePh = us * ph
    print(valuePh)

phP = 51.36
usD = 1

# none return function
print(converterVoid(phP,usD))
converterVoid(phP,usD)
converterVoid(phP,usD)

# function using conditional statement
arrayList = [1, 2, 3 , 4 ,5]
arrayDict = {"one": 1, "two": 2, "three": 3}

def meanWithCondition(dataType):
    if isinstance(dataType, dict): # 
        print(type(dataType), dataType)
        phpValue = sum(dataType.values()) / len(dataType)
    else:
        print(type(dataType), dataType)
        phpValue = sum(dataType) / len(dataType)
    
    return phpValue

meanValue = meanWithCondition(arrayList)
print(meanValue)
meanValue = meanWithCondition(arrayDict)
print(meanValue)
