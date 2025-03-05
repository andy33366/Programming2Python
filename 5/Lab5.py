#main function

from ToyFactory import ToyFactory

factory = ToyFactory()

def main():
    #while message is blank
    stop = False
    
    while(not stop):
        
        name = input("Enter the name of your new toy: ")
        label = input("Enter your address: ")
        
        #attempt to make a toy
        try:
            toy = factory.makeToy(name, label)
            print("Say hello to " + toy.getContent().getName() + ", your new toy! It is being delivered to " + toy.getLabel())

        #if error --> print error statement and end loop
        except:
            print(factory.getMessage())
            stop = True

main()
