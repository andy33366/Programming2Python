#lets user input grades until they provide sentinel value of -1
#prints entire list and the average

def main():

    grades = []

    userInput = int(input("Please enter a grade: "))

    while (userInput != -1):
        grades.append(userInput)
        userInput = int(input("Please enter a grade: "))

    print(grades)
    print("The average is "+str(sum(grades)/len(grades)))

main()

