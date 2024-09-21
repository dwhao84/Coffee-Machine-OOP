from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu          = Menu()          # Call Menu's Class
coffee_maker  = CoffeeMaker()   # Call coffee_maker's Class
money_machine = MoneyMachine()  # Call MoneyMachine's Class

while is_on:
    options = menu.get_items() # Call get_items() 找到飲料種類
    choice = input(f"What would you like? ({options})").lower()
    # 用Choice得到輸入的內容。
    
    # 當使用者輸入off時，則停止。
    if choice == "off":
        is_on = False
        
    # 當使用者輸入report時，則 顯示相關report。
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    
    else:
        # 找到飲料的內容，帶入choice以後。
        drink = menu.find_drink(choice)
        
        # 確認下列是否有滿足以下條件
        # 1. 用 is_resource_sufficient()，確認是否製作飲料的資源有足夠。
        # 2. 當條件滿足之後，用 make_coffee()，回傳製作結果。
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                
            
        
        
        
    
