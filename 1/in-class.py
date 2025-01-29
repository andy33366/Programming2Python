import random


#sets user choice to continue/ y for yes, n for no
choice = "y"

def guessingGame():
    
    print("Guess which number between 1 and 100 I am thinking of.")

    # generates random number between 1 and 100
    rand = random.randint(1, 100)

    # takes user input
    userinput = int(input("Enter an integer between 1 and 100: "))

    #keeps player in the while loop until they guess the correct number
    while True:
        if userinput < rand:
            #if the user guesses too low they are prompted to guess again
            print("Too low!")
            userinput = int(input("Enter an integer between 1 and 100: "))
        elif userinput > rand:
            #if the user guesses too high they are prompted to guess again
            print("Too high!")
            userinput = int(input("Enter an integer between 1 and 100: "))
        else:
            #once they guess correctly the loop ends
            print("correct!")
            break

#with a sentinel value of "n" the player is prompted at the end of each game if they would like to continue
while (choice != "n"):
    guessingGame()
    choice = input("Would you like to continue playing? (y/n): ")
    while (choice != "y" and choice != "n"):
        choice = input("Invalid input. Please enter either \"y\" to continue or \"n\" to end the game: ")


    
