from abc import ABC, abstractmethod

#creates the abstract Bird class
class Bird(ABC):

    def __init__(self, name):
        self.name = name

    #getter and setter
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def __str__(self):
        print(f"This is a(n) {self.name}")

    @abstractmethod
    def eat(self):
        pass
