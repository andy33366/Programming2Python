#crustacean
from abc import ABC, abstractmethod

class Crustacean(ABC):
    def __init__(self, name, legs, claws):
        self.name = name
        self.legs = legs
        self.claws = claws

    #getters
    def getName(self):
        return self.name
    def getLegs(self):
        return self.legs
    def getClaws(self):
        return self.Claws
    #setters
    def setName(self, name):
        self.name = name
    def setLegs(self, legs):
        self.legs = legs
    def setClaws(self, claws):
        self.claws = claws

    def __str__(self):
        no = ""
        if not self.claws:
            no = "no"
        print(f"{self.name} has {self.legs} legs and {no} claws")

    @abstractmethod
    def swim(self):
        pass
