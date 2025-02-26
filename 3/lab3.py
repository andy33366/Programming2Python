from Member import Member
from datetime import datetime


def main():
    
    member1 = Member("Jane", datetime(1999, 5, 4), 120, 60)
    member2 = Member("John", datetime(2000, 12, 20), 150, 72)

    print("The BMI for " + member1.getName() + " (" + str(member1.getAge()) + ") is " + format(member1.getBMI(), ".2f") + " - " + member1.getMessage()) 
    print("The BMI for " + member2.getName() + " (" + str(member2.getAge()) + ") is " + format(member2.getBMI(), ".2f") + " - " + member2.getMessage()) 

main()
