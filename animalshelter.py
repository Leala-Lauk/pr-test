#Author: Leala Laukkonen
#Date: September 30, 2026
animal_names=['Margaret', 'Rem', 'Jim']                                         #OG names list
CAPACITY=5                                                                      #Capacity value

def add_animal(name, species):
    if len(animal_names)>=CAPACITY:                                             #if/else shelter is at capacity value
        print("Shelter is at capacity, we cannot accept any more animals.")
    else:
        animal_names.append(name)                                               #within capacity=add to list
        print("Welcome "+ name +" the "+ species +"!")

def adopt_animal(name):
    if name in animal_names:                                                    #if/else name value in names list
        print(name +" has been adopted! Congratulations, "+ name +"!")
        animal_names.remove(name)                                               #name in list=remove via name
    else:
        print("Name not found in animal index. Please try again.")

def get_animal_count():
    if not animal_names:                                                        #if/else count names list
        print("Total: 0")
        return 0                                                                #if shelter empty
    else:
        print("Total: "+ str(len(animal_names)))                                #read list length
        return len(animal_names)

def find_animal(name):
    if name in animal_names:                                                    #if/else locate index in name list
        print("Index found: "+ str(animal_names.index(name)))                   #read name for index in list
        return animal_names.index(name)
    else:
        print("Index not found.")                                               #if name is not in list
        return -1

add_animal('Fig', 'Rabbit')
add_animal('Otter', 'Hamster')
add_animal('Sol', 'Cat')
get_animal_count()
adopt_animal('Margaret')
get_animal_count()
find_animal('Fig')