
class Exhibit:
    def __init__(self, name, temp, humid):
        self.name = name
        self.temp = temp
        self.humid = humid

    #Getters
    def getName(self):
        return self.name

    def getTemp(self):
        return self.temp

    def getHumid(self):
        return self.humid

    #setters
    def setName(self, name):
        self.name = name

    def setTemp(self, temp):
        self.temp = temp

    def setHumid(self, humid):
        self.humid = humid

    def __str__(self):
        print(f"\nThis is a(n) {self.name}.\nThe temperature is {self.temp} degrees F.\nThe humidity is {self.humid}%.")

