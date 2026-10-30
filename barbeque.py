#Author: Leala Laukkonen
#Date: September 9, 2026
customer_name=input('Please enter your name: ')                 #set customer name var.
sandwich_price=8                                                #set Meals' price value
platter_price=12
meal_choice=input('Do you want a Sandwich Meal or Platter Meal? (sandwich/platter): ')
if meal_choice.lower()=='sandwich':                             #^create 2 input options+other
    meal_price=sandwich_price                                   #set meal_price to price value
elif meal_choice.lower()=='platter':
    meal_price=platter_price
else:
    print('Invalid choice. Defaulting to Sandwich Meal')        #other input: default to sandwich option
    meal_choice='Sandwich'
    meal_price=sandwich_price
num_meals=int(input('How many Meals would you like? '))         #set meal amount # value
total_cost=meal_price*num_meals
extra_sauce=input('Would you like extra sauce with that? (yes/no): ')
if extra_sauce.lower()=='yes':                                  #^create yes input option
    total_cost+=0.5*num_meals                                   #if true, add .5 to each meal # value
original_total=meal_price*num_meals
sauce_added=extra_sauce.lower()=='yes'                          #sauce_added='True' if input='yes'

print(' ')                                                      #(gap to make it look nicer)
print('Order Summary: ')                                        #print all input results
print('Customer:', customer_name)
print('Meal Type: '+meal_choice+' meal')
print('Number of Meals: '+str(num_meals))                       #convert # value to str
print('Extra Sauce? '+('Yes'if sauce_added else 'No'))
print('Original Total: $'+'{:.2f}'.format(original_total))      #convert # value to float w/ 2 decimals
print('Final Total: $'+'{:.2f}'.format(total_cost))             #^