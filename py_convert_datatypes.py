# CONVERTING DATATYPES

# list to tuple
lstNumber = [1, 2 ,3]
print(lstNumber)
print(type(lstNumber))

tupNumber = tuple(lstNumber)
print(tupNumber)
print(type(tupNumber))

lstPersonInfo = [["firstname", "rom"], ["lastname", "pilapil"]]
print(lstPersonInfo)
print(type(lstPersonInfo))

dctPersonInfo = dict(lstPersonInfo)
print(dctPersonInfo)
print(type(dctPersonInfo))

# LIST TO TUPLE
numberList = [1, 2, 3, 4]
numberTuple = tuple(numberList)
print(numberList, type(numberList))
print(numberTuple, type(numberTuple))

#TUPLE TO LIST
numberTuple = (1, 2, 3, 4)
numberLst = list(numberTuple)
print(numberTuple, type(numberTuple))
print(numberList, type(numberList))

# USING JOIN IN STRING
stringList = ['r', 'o', 'm', 'w', 'i', 'l']
stringJoin = str.join("-", stringList)
print(stringJoin)