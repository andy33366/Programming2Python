import random

def main():

    sum = 0

    for i in range(10):
        # generates random number between 1 and 100
        rand = random.randint(1, 100)
        print(rand, " + ")
        sum += rand
    
    print(sum)

