#main function

from ToyFactory import ToyFactory

factory = ToyFactory()

def main():
    #while message is blank
    stop = False
    
    while(not stop):
        
        name = input("Enter the name of your new toy: ")
        
        #attempt to make a toy
        try:
            toy = factory.makeToy(name)
            print("Say hello to " + toy.getName() + ", your new toy!")

        #if error --> print error statement and end loop
        except:
            print(factory.getMessage())
            stop = True

main()
