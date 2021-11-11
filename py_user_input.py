# USER INPUT

def weatherTemp(temp):
    if temp > 22:
        return "warm"
    else:
        return "cold"
    
userInput = float(input("enter temp: "))
print(weatherTemp(userInput))