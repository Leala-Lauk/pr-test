#Name: Leala Laukkonen
#Date: October 28, 2026

toppings=["Extra Patty", "Bacon", "Roast Beef", "American Cheese", "Romaine Lettuce", "Tomatoes", "Onions", "Pickles",  #list of toppings
          "Jalapenos", "Cucumber", "Fried Egg", "Ketchup", "Mustard", "BBQ Sauce", "Mayo"]
sides=["Fries", "Waffle Fries", "Mashed Potatoes", "Mac n' Cheese", "Seasonal Fruit"]                                   #list of sides
prices={"Extra Patty": 2.00, "Bacon": 2.00, "Roast Beef": 3.50, "American Cheese": 1.00, "Romaine Lettuce": 0.50,       #dictionary for all prices
        "Tomatoes": 0.50, "Onions": 0.40, "Pickles": 0.40, "Jalapenos": 0.60, "Cucumber": 0.40, "Fried Egg": 1.00,
        "Ketchup": 0.20, "Mustard": 0.20, "BBQ Sauce": 0.30, "Mayo": 0.20, "Fries": 1.50, "Waffle Fries": 1.50,
        "Mashed Potatoes": 1.50, "Mac n' Cheese": 1.50, "Seasonal Fruit": 1.00, "No Toppings": 0.00, "burger": 10.00}
order=[]                                                                                                                #empty order + 'burger' lists, add inputs
burger=[]

greeting="Welcome to Burgers to Go! Build Your Own Burgers, Your Way. \nTime to build a burger!"
goodbye="Thank you for your patronage, enjoy your meal!"

def display(options):                                                                                   #FUNC: to display all toppings or sides
    if options==sides:                                                                                                  #extra formatting
        print(" ")
    number=0
    for option in options:                                                                                              #for loop through all list items
        number+=1                                                                                                       #change from index format
        print(f"{number}. {option} (${prices[option]:.2f})")

def get_order():                                                                                                        #FUNC: main func to start+add new 'burgers'
    print("\n(Enter 0 to continue)")
    add_order()                                                                                                         #jump to next function
    new_burg=input("Would you like to add another burger to your order? (Y/N): ")
    if new_burg.lower()=="y":
        return get_order()                                                                                              #if yes, repeat from top; or end to receipt
    else:
        return None

def add_order():                                                                                                        #FUNC: collect all items in 'burger' list
    while True:                                                                                                         #while loop, keep asking until break
        try:
            choice = input("What type of topping do you want? (Enter the number): ")
            choice = int(choice)                                                                                        #str to int
            if choice==0:
                if not burger:                                                                                          #if empty list, clarify 'no toppings'; or ignore
                    burger.append("No Toppings")
                burger_end()
                side_option = input("Would you like to add a side? (Y/N): ")
                if side_option.lower() == "y":                                                                          #if yes, display options and next function; or ignore
                    display(sides)
                    side_choice()
                order.append(burger.copy())                                                                             #create copy of 'burger' list in order list
                burger.clear()                                                                                          #clear after copy is recorded for new 'burger' info
                break                                                                                                   #return to main func
            else:
                choice -= 1
                burger.append(toppings[choice])                                                                         #add option to list and loop
        except (IndexError, ValueError):                                                                                #expected exceptions, back to loop
            print("Item not found, please try again.")

def burger_end():                                                                                                       #FUNC: final toppings display
    print("\nYour burger is topped with: ")
    for topping in burger:                                                                                              # for loop, all toppings in 'burger'
        print(" - " + topping)

def side_choice():                                                                                                      #FUNC:(optional) add side to 'burger'
    print("\n(Enter 0 to skip)")
    choice = input("What side would you like? (Enter the number): ")
    try:
        choice = int(choice)                                                                                            #in 'try' to prevent errors
        if choice == 0:
            pass                                                                                                        #option to skip if mistake 'y'
        else:
            choice -= 1
            burger.append(sides[choice])                                                                                #add option to list and return to end of loop
    except (IndexError, ValueError):                                                                                    #expected errors
        print("Item not found, please try again.")                                                                      #ask until valid input
        return side_choice()

def print_order():                                                                                                      #FUNC: print all info as formatted 'receipt'
    print("\n\nRECEIPT")
    burger_count = 0                                                                                                    #count to number 'burgers' lists
    total=0                                                                                                             #total of all items
    for burger in order:                                                                                                #for loop; all 'burger' lists in order list
        burger_count+=1
        print(f"{'\nBURGER '+ str(burger_count):<30} ${prices["burger"]:.2f}")                                            #formatting gap/decimals, int to str, dictionary use
        subtotal=prices["burger"]                                                                                       #dictionary use for easy changes
        for topping in burger:                                                                                          #for loop; all items in 1 'burger'
            if topping in sides:                                                                                        #distinguishing sides formats
                print(f"   + {topping:<25} ${prices[topping]:.2f}")
                subtotal+=prices[topping]                                                                               #add all prices to subtotal
            else:                                                                                                       #regular toppings formats
                print(f" - {topping:<27} ${prices[topping]:.2f}")
                subtotal += prices[topping]
        print(f"{"subtotal":<30} ${subtotal:.2f}")
        total+=subtotal                                                                                                 #add all subtotals to total
    print("--------------------------------------")
    print(f"{"TOTAL":<30} ${total:.2f}")

print(greeting)                                                                                                         #final outputs
display(toppings)
get_order()
print_order()
print(goodbye)