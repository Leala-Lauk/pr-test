fuel=100
planets_visited=0
alien_encounters=0
alien_friends=['Zorg','Blip','Glorp','Xena','Quark']

print('Welcome aboard your new ship, The Python Explorer!')
print('Initial fuel: ')
print(fuel)
print('Mission 18: Visit 5 new planets.')
print('   Mission 18.1: Meet 3 aliens.')

while fuel > 0 and planets_visited < 5:
    print('\nCurrent fuel: '+str(fuel))
    print('Planets visited: '+str(planets_visited))

    fuel-=20
    planets_visited+=1

    print('>Visiting new planet...')

print('\nMission status...')
if planets_visited >= 5:
    print("Success! We'll send a return pod to you soon.")
    print("\nDon't forget to meet some aliens!")
    for alien in alien_friends:
        if alien_encounters >= 3:
            break
        print('You meet ' + alien + '!')
        alien_encounters += 1
else:
    print("You've only reached "+str(planets_visited)+' planet(s).')
    print("Mission failed. You're dead to us.")
