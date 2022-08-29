# CONDITIONAL STATEMENT

# using if statement
x = [1, 3, 5, 7]
y = {"one": 1, "two": 2, "three": 3}

if type(x) == dict:
    ave = sum(x.values()) / len(x)
    print(ave)
    
# using else statement
if type(x) == dict:
    ave = sum(x.values()) / len(x)
    print(ave)
else:
    x = sum(x) / len(x)
    print(x)
    
# isinstance condition
if isinstance(y, dict):
    print("y is dictionary")
else:
    print("y is not a dictionary")
    
# comparison conditions
a = 10
b = 8

if a > b:
    print("b is greater than a")
else:
    print("b is not greater than a")

if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")
    
print("Done program")

# elif statement
num1 = 22
num2 = 7

if num1 > num2:
    print("num1 is greater")
elif num1 < num2:
    print("num1 is less")
else:
    print("num1 and 2 are equal")
    
# using boolean operators "and" & "or"
number1 = 26
number2 = 22

if number1 < 30 and number2 > 20:
    print("Both true")
    
if number1 < 30 or number2 < 20:
    print("1 is true")
