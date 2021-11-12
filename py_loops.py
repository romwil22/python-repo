#  FOR & WHILE LOOPS

# for looop
names = ["ana", "rom", "steven", "rj"]

# print name
for name in names:
    print(name)
    
# round off temperature value
temp = [31.4, 36.6, 27.2, 35.8]
for t in temp:
    print(round(t))
    

# for loop using dictionary
nameGrade = {"ana": 2.0, "rom": 2.25, "steven": 1.75, "rj": 1.5}

# iterate tuple of key, value pair
for nG in nameGrade.items():
    print(nG)
    
# iterate values in dictionary
for v in nameGrade.values():
    print(v)
    
# iterate keys in dictionary
for k in nameGrade.keys():
    print(k)