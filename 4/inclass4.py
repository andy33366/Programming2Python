from Chef import Chef
from Meal import Meal

def main():
    mealName = input("Enter the name of your meal: ")
    chef = Chef()
    meal = chef.makeMeal(mealName)
    print(f"You ordered {meal.getName()}.")

main()
