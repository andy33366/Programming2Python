from Chef import Chef
from Meal import Meal
from ToGo import ToGo

def main():
    mealName = input("Enter the name of your meal: ")
    customerName = input("Enter who this meal is for: ")
    chef = Chef()
    meal = chef.toGoMeal(customerName, mealName)
    print(f"{meal.getCustomerName()} ordered {meal.getMealName()}.")

main()
