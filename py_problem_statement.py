# PROBLEM STATEMENT

def sentenceMaker(phrase):
    interrogatives = ("How", "What", "Why")
    capitalized = phrase.capitalize()
    if capitalized.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

messageLst = []

while True:
    userInput = input("say something: ")
    
    if userInput == "\end":
        break
    else:
        messageLst.append(sentenceMaker(userInput))
        
print(" ".join(messageLst))