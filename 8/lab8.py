from Penguin import Penguin
from Bird import Bird

def main():

    #instantiating the Bird class creates an error because it is an abstract class and cannot be instatiated directly, it must be done through a subclass
    #bird = Bird("pidgeon")

    #creates an object of the Penguin class
    gueeny = Penguin()

    #runs the Penguin class's methods
    gueeny.__str__()
    gueeny.fly()
    gueeny.eat()
    gueeny.swim()

main()
