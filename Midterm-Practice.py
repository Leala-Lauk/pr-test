tortillas=["Corn", "Flour", "Whole Wheat", "Gluten-Free"]                                                       #all ingredients in categories
fillings=["Black Beans", "Brown Beans", "Chicken", "Fish", "Beef", "White Rice", "Brown Rice",
          "Mexican Rice"]
toppings=["Onions", "Lettuce", "Tomatoes", "Cheese", "Red Salsa", "Green Salsa", "Sour Cream", "Jalapeños",
          "Guacamole"]
order=[]                                                                                                        #empty list to add to later

def display_options(options, title):                                                        # * function to display options (list, string)
    print(title +":")
    number=0
    for option in options:                                                                                      #loop through every option
        number+=1                                                                                               #number ref for list
        print(str(number) +". "+ option)                                                                        #str convert to keep string together

def get_choice(options):                                                                     # * function to ask for order details
    choice=input("Please enter the number of your choice: ")
    choice=int(choice)                                                                                          #int conversion for equation
    try:
        choice -= 1                                                                                             #converting list number to index number
        order.append(options[choice])                                                                           #add option to empty list above for later
        print(options[choice] +" has been added to your order.")
        if options==toppings:                                                                                   #optional path for multiple topping choices
            more=input("Would you like to add another topping? (y/n): ")
            if more=="y":                                                                                       #if else loop or end
                return get_choice(toppings)
            else:
                return options[choice]
        print(" ")
        return options[choice]
    except IndexError:                                                                                          #except for if an invalid number is typed
        print("That is not one of the options, please try again.")
        return get_choice(options)

def print_order(order):                                                                 # * added function to group up order printing
    print("\nYour Order: ")
    print("- "+ order[0] +" tortilla")                                                                          #order[0] and order[1] are constant
    print("- "+ order[1])
    for top in order[2:]:                                                                                       #loop for all items past order[1], must be toppings
        print("- "+ top)
    if "Red Salsa" in order:                                                                                    #optional comment if salsa items are chosen
        print("One spicy salsa taco coming right up!")
    elif "Green Salsa" in order:
        print("One spicy salsa taco coming right up!")
    else:
        print("One taco coming right up!")

print("Welcome to Catrinas Mexican Grill! \nBuild your own taco! \n ")                                          # * interactable section
display_options(tortillas, "Tortillas")
get_choice(tortillas)
display_options(fillings, "Fillings")
get_choice(fillings)
display_options(toppings, "Toppings")
get_choice(toppings)
print_order(order)
print("Thank you for ordering from Catrinas Mexican Grill!")