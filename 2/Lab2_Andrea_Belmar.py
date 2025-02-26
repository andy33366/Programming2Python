
compParts = []

userInput = 0

#add parts
def addParts(compParts):
    compParts.append(input("Please enter the name of the part to add: "))

#remove parts
def removeParts(compParts):
    compParts.remove(input("Please enter the name of the part to remove: "))

#view parts
def viewParts(comParts):
    for i in compParts:
        print(i)

print("Welcome! This program keeps track of computer parts. \n\n")

while userInput != 4:
    userInput = int(input("enter 1 to add a part\nenter 2 to remove a part\nenter 3 to view parts\nenter 4 to quit the program\n"))
    if userInput == 1:
        addParts(compParts)
    elif userInput == 2:
        removeParts(compParts)
    elif userInput == 3:
        viewParts(compParts)
    elif userInput == 4:
        break
    else:
        userInput = int(input("invalid input!\nenter 1 to add a part\nenter 2 to remove a part\nenter 3 to view parts\nenter 4 to quit the program"))
        


