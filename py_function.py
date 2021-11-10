# CREATING USER FUNCTION

# calculating average in the list function

# returning value
def aveFunc(lstnumbers):
    average = sum(lstnumbers) / len(lstnumbers)
    return average

# void return none value
def aveFuncV(lstnumbers):
    average = sum(lstnumbers) / len(lstnumbers)
    print("average:", average)

lstnum = [2, 5, 8, 15, 23]

aveFuncV(lstnum)
ave = aveFunc(lstnum)
print("average:", ave)