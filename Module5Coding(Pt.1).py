import random
goldfish = ["Snap", "Chip", "Honey", "Cosmic", "Lime"]

print("Welcome to the Goldfish Playdate Planner!")
print("Your Goldfish's friends are: "+", ".join(goldfish))

new_fish=input("\nEnter the name of your new fish: ")
if new_fish:
    goldfish.append(new_fish)

print("Updated role call: "+", ".join(goldfish))

fish_to_remove=input("\nEnter the name of a fish you want to remove: ")
if fish_to_remove in goldfish:
    goldfish.remove(fish_to_remove)
    print(fish_to_remove + " is a bad influence on your goldfish and has been removed from",
          "the list because of this.")
    print("Updated role call: " + ", ".join(goldfish))
else:
    print("Sorry, "+fish_to_remove + " is not on the list.")
    print("The list remains unchanged.")

print("\n<3 Let's set up some 2-fish playdates! <3")
random.shuffle(goldfish)
for i in range(0, len(goldfish), 2):
    if i+1<len(goldfish):
        print(goldfish[i] +" will have a playdate with "+ goldfish[i+1] +"!")
else:
    print(goldfish[i] +" will have to play alone for now.")

print(" ")
playdate_schedule=[]
for i in range(len(goldfish)):
    day=input("Enter a day for "+ goldfish[i] +"'s playdate: ")
    playdate_schedule.append(day)

print("\nPLAYDATE SCHEDULE: ")
for i in range(len(goldfish)):
    print(goldfish[i] +" has a playdate on "+ playdate_schedule[i])

search_fish=input("\nEnter a fish's name to find it's playdate: ")
if search_fish in goldfish:
    index=goldfish.index(search_fish)
    print(search_fish +" has a playdate on "+ playdate_schedule[index] +"!")
elif search_fish == fish_to_remove:
    print(fish_to_remove + " was removed for a reason.")
else:
    print("Sorry, "+ search_fish +" is not on the list.")