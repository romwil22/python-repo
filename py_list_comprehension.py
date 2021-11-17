# LIST COMPREHENSION

tempLst = [330, 364, 290, 250, -10]
newTempLst = []

# using iterattion
for t in tempLst:
    newTempLst.append(t/ 10)
    
print(newTempLst)

# using list comprehension

comTempLst = [t / 10 for t in tempLst]
print(comTempLst)

# using if contidion in list comprehension
comIfTempLst = [t / 10 for t in tempLst if t > 0]
print(comIfTempLst)

# using if else condition in lst comprehension
comIfTempLst = [t / 10 if t > 0 else 0 for t in tempLst]
print(comIfTempLst)