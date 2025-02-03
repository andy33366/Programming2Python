# this program will provide random addition and subtraction questions until the stutent quits
import random


cont = True
correct = 0
counter = 0

def mathGame():
    
    global correct


    #generates 2 random integers between 1 and 10
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)

    #decide between addition and subtraction
    addOrSub = random.choice([True, False])
    if True:
        #addition
        print(str(num1) + " + " + str(num2) + " = ")
        answer = num1 + num2
    else:
        #subtraction
        #if the answer will be negative, swap num1 and num2 to make the answer positive
        if (num1 < num2):
            temp = num1
            num1 = num2
            num2 = temp
        print(str(num1) + " - " + str(num2) + " = ")
        answer = num1 - num2
    #gets user's answer
    userInput = input()
    #ends while loop if user wants to quit
    if (userInput == "quit"):
        return False
    #gives feedback on correct/incorrect answer
    if (int(userInput) == answer):
        correct += 1
        print("Correct!")
    else:
        print("Incorrect! The correct answer is " + str(answer))

    #continues the while loop
    return True

#large loop that check if student wants to quit
while(cont):
    counter += 1
    cont = mathGame()
    #enter quit to end the game

print("You got " + str(correct) + " questions out of " + str(counter) + " correct!")
    
