# HANDLING ERRORS

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "undefine"
    
def add(x, y):
    try:
        return x + y
    except TypeError:
        return "string argument cannot add"
    
def concatenate(x, y):
    try:
        return x + y
    except TypeError:
        return "int argument cannot concatenate"

print(divide(2, 4))
print(divide(2, 0))
print(add(12, 32))
print(add(12, "21"))
print(concatenate("python ", "programming"))
print(concatenate(1, "23"))