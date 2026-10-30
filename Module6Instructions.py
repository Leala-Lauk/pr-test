tax_rate=0.085
menu_items=['burger', 'fries', 'drink']
burger_price=4.99
fries_price=2.49
drink_price=1.29

def add_ingredient():
    if input("Would you like to add anything? (yes/no) ")=="yes":
        ingredient=input("What would you like to add? ")
        print("Adding "+ ingredient +" to your burger!")

def calc_combo_price(has_burger, has_fries, has_drink):
    subtotal=0
    if has_burger:
        subtotal+=burger_price
    if has_fries:
        subtotal+=fries_price
    if has_drink:
        subtotal+=drink_price

    tax=tax_rate*subtotal
    total_cost=round(subtotal+tax, 2)
    print("Total Combo Price: $"+ str(total_cost))
    return total_cost

def order_decision():
    supersize=input("Would you like to supersize your item? (yes/no): ")
    if supersize.lower() == "yes":
        print("Great choice! Go big or go home!")
        return True
    elif supersize.lower() == "no":
        print("Remember, life is short--try a large next time!")
        return False

def order_food(menu):
    if not menu:
        print("Your order is complete. Enjoy your meal!")
        return
    else:
        input("Would you like to order a "+ menu.pop(0) +"? ")
        order_food(menu)

order_food(menu_items)