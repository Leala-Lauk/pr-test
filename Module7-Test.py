                                                                            # Dictionaries
food_stands={"Pronto Pup": "Corn Dog", "Big-Pig": "Bacon-on-a-Stick",
             "Chimborazo": "Empanada", "Mami Churros": "Churros", "Mouth Trap": "Cheese Curds",
             "Que Viet": "EggRoll-on-a-Stick", "Tot Boss": "Tater Tots"}
print("Last year's Food Stands at the Fair: ")
for stand, food in food_stands.items():
    print(stand +": "+ food)

food_stands["Fresh French Fries"]="Fries"
food_stands["Pronto Pup"]="Footlong Corn Dogs"
del food_stands["Big-Pig"]

print("\nThis year's Food Stands: ")
for stand, food in food_stands.items():
    print(stand +": "+ food)
                                                                            #Tuples
attractions=[("Giant Slide", "East of the Grandstand"), ("Skyride", "Near Dan Patch Ave"),\
             ("Adventure Park", "South of the Grandstand"), ("Go Carts", "South of Nelson St")]
print("\nOG Fair Attractions: ")
for attraction in attractions:
    print(attraction[0] +" is located "+ attraction[1])

new_attraction=("Haunted House", "Near the Midway")
attractions.append(new_attraction)
print("\nAll attractions this year: ")
for attraction in attractions:
    print(attraction[0] +" is located "+ attraction[1])
                                                                            #Sets
activities={"Riding down Giant Slide", "Watching the Parade", "Visiting Butterfly House",
            "Watching Reptile Show", "Ride Ferris Wheel", "Climbing Rock Wall", "Walking through Haunted House",
            "Listen to Concert", "Riding the Thunderbird", "Riding the Slingshot", "Watching the Horses"}
print("\nLast year's activities: ")
print(activities)

activities.add("Watching the Parade")
print("\nPrototype activities: ")
print(activities)
activities.remove("Riding down Giant Slide")
print("\nThis year's activities: ")
print(activities)
                                                                            #Schedule
daily_planner={"Morning": [("Breakfast", food_stands["Que Viet"]), ("Activity", list(activities)[0])],
               "Midday": [("Lunch", food_stands["Pronto Pup"]), ("Attraction", attractions[3][0] +" located "+ attractions[3][1])],
               "Evening": [("Dinner", food_stands["Chimborazo"]), ("Activity", list(activities)[1])],}
print("\nMy MN State Fair Day Planner: ")
for time, plans in daily_planner.items():
    print(time +":")
    for plan in plans:
        print("- "+ plan[0] +": "+ plan[1])