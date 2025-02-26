from Meal import Meal

class ToGo:
    def __init__(self, name, mealName):
        #
        self.customerName = name
        self.meal = Meal(mealName)

    def getCustomerName(self):
        return self.customerName

    def getMealName(self):
        return self.meal.getName()
