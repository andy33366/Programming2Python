from datetime import datetime

class Member:
    def __init__(self, name, dob, weight, height):
        self.name = name
        #calculates age in years based on date of birth
        self.age = datetime.today().year - dob.year - ((datetime.today().month, datetime.today().day) < (dob.month, dob.day))
        #in kg
        self.weight = weight * 0.45359237
        #in meters
        self.height = height * 0.0254

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getWeight(self):
        #returns pounds
        return self.weight * 2.2046

    def getHeight(self):
        #returns inches
        return self.height * 39.3701

    def setWeight(self, weight):
        self.weight = weight

    #calculates BMI based on formula
    def getBMI(self):
        return self.weight/(self.height ** 2)

    def getMessage(self):
        BMI = self.getBMI()
        if BMI < 18.5:
            message = "Underweight"
        elif 18.5 <= BMI < 25.0:
            message = "Normal"
        elif 25.0 <= BMI < 30.0:
            message = "Overweight"
        elif 30.0 <= BMI:
            message = "Obese"
        else:
            message = "error"
        return message





