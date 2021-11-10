# LIST

# LIST STORING MULTIPLE VALUES
lstNumber = [1, 2, 3 ,4 ,5]
print(lstNumber)

# LIST SLICES
print(lstNumber[:3])
print(lstNumber[2:])
print(lstNumber[1:3])

# GETTING VALUE USING INDEX
print(lstNumber[0])
print(lstNumber[2])
print(lstNumber[4])

# ADD VALUE IN A LIST
lstNumber.append(6)
print(lstNumber)

# FINDING INDEX VALUE
print(lstNumber.index(3))

# CHANGE VALUE OF AN INDEX
lstNumber[2] = 33
lstNumber[0] = 11
print(lstNumber)

# NEGATIVE INDEX AND SLICES
print(lstNumber[-1])
print(lstNumber[-4])
print(lstNumber[-3:])
print(lstNumber[-4:-2])

# REMOVE VALUE IN THE LIST
lstNumber.remove(4)
print(lstNumber)

# CLEAR LIST
lstNumber.clear()
print(lstNumber)