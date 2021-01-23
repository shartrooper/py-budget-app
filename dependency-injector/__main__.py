# Built-in modules
import sys
# app modules
from containers import Container
sys.path.append('../')
from budget import create_spend_chart


if __name__ == '__main__':
    container = Container()
    
    food= Container.user_category("Food")
    clothing= Container.user_category("Clothing")
    auto = Container.user_category("Auto")
    
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print("Food balance prior transfer: "+str(food.get_balance()))
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    print(food)
    print(clothing)
    print(auto)
    print(create_spend_chart([food, clothing, auto]))
