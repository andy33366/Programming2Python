from Meal import Meal 
from ToGo import ToGo

class Chef:
    def makeMeal(self, mealName):
        return Meal(mealName)
    def toGoMeal(self, name, mealName):
        return ToGo(name, mealName)
