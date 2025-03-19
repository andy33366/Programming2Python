

class Bug:
    def __init__(self, name = "Bug", legs = 4, wings = 2):
        self.name = name
        self.legs = legs
        self.wings = wings

    def getName(self):
        return self.name

    def getLegs(self):
        return self.legs

    def getWings(self):
        return self.wings

    def setName(self, name):
        self.name = name

    def setLegs(self, legs):
        self.legs = legs

    def setWings(self, wings):
        self.wings = wings
    def __str__(self):
        print(f"The {self.name} has {self.legs} legs and {self.wings} wings. ")
    
