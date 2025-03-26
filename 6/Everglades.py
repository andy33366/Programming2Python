from Exhibit import Exhibit

#inherits from exhibit
class Everglades(Exhibit):
    def __init__(self, water, name = "Everglades", temp = 80, humid = 90):
        super().__init__(name, temp, humid)
        self.water = water

    def getWater(self):
        return self.water

    def setWater(self, water):
        self.water = water

    def __str__(self):
        #uses the __str__ from the superclass then adds in waterlevel
        super().__str__()
        print(f"The water level is {self.water}.")
