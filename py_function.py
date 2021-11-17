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
    
# multiple argument
def voltage(i, r):
    return i * r

# Default and Non-default Parameters and Keyword and Non-keyword Arguments
def current(v = 0, r=1):
    return v / r

# *args parameter
def mean(*args): # tuple datatype
    return sum(args) / len(args)

# kwargs parameter
def dctStorage(**kwargs):
    return kwargs

lstnum = [2, 5, 8, 15, 23]

aveFuncV(lstnum)
ave = aveFunc(lstnum)
print("average:", ave)
print("voltage:", voltage(2, 10))
print("current:", current())
print("current", current(r= 20, v= 12))
print("current:", current(220, 1000))
print("mean:", mean(2, 5, 10, 15, 21))
print("dictonary:", dctStorage(x = 2, y = 6, z = 4))

