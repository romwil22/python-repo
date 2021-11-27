# MODULES

import os
import time
import pandas

def readFile():
    if os.path.exists("fruits.txt"):
        
        with open("fruits.txt", 'r') as readTextFile:
            print("fruits:\n")
            for l in readTextFile:
                print(l)
                time.sleep(2)
    else:
        print("file not found")

def checkPath():
    filePath = os.path.exists("fruits.txt")
    print(filePath)
    

def readCsvFile():
    if os.path.exists("temps_today.csv"):
        
        with open("temps_today.csv") as readCsvFile:
            data = pandas.read_csv("temps_today.csv")
            print(data)
            print(data.mean())
    else:
        print("file not found")


#readFile()
#checkPath()

readCsvFile()
