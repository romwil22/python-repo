"""Implement a function that:

(1) takes a list and another object as parameters

(2) checks if that object is in the list

(3) adds the object to the list if the object is not in the list

(4) returns the list."""

def checkObj(lst,obj):
    
    if obj not in lst:
        lst.append(obj)
        return lst
    else:
        return lst
    
print(checkObj([1,2,3,4,5],15))
