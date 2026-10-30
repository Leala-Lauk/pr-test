#Author: Leala Laukkonen
#Date: August 22, 2026
import random                                                                                   #imports+lists first
excitements=["Great!", "Amazing!", "Lovely!", "Grand!", "Ok.", "Awesome!", "Another!", "Perfect!"] #excitements list, 8
dad_jokes=["Don't buy anything with velcro.\nIt's a total ripoff!",                             #dad jokes list, 11
           "How much does a chimney cost?\nNothing, it's on the house!",
           "Dogs can't operate MRI machines.\nHowever, catscan!",
           "I only remember 25 letters of the alphabet.\nI don't know y!",
           "I finally decided to sell my vacuum.\nAll it was doing was gathering dust!",
           "I cry every time I boil food for dinner.\nThe water will be mist!",
           "If the boat you're riding tips over, wear it as a hat.\nIt'll be cap-sized!",
           "Yesterday, my kid asked for a book mark.\nCan't believe they still haven't learned my name!",
           "How are skeletons so chill?\nNothing can get under their skin!",
           "Why did the dog run after the book?\nDogs are always chasing tales!",
           "What do you get when you cross a joke with a rhetorical question?\n..."]

print("You've come to hear some japes and jests?")
print("We've curated up to "+ str(len(dad_jokes)) +" fatherly jokes.",
        "Here's 4, just for you:\n ")                                                           #convert list len/int to str
random.shuffle(dad_jokes)                                                                       #shuffle before loop to prevent repeats
for i in range(0,4):                                                                            #'for' loop, 4 jokes
    print(dad_jokes[i] +"\n ")

while True:                                                                                     #initiate loop
    user_choice=input("Would you like to hear another? (yes/no) ")
    if user_choice=="yes":
        random.shuffle(dad_jokes)                                                               #reshuffles to not repeat
        random.shuffle(excitements)
        print("\n"+ excitements[i] +"\n" + dad_jokes[i] +"\n")                                  #format answers with new lines
        continue                                                                                #repeat from 'while'
    else:
        break                                                                                   #stop 'while' loop

print("This jester's performance has finished, thank you for listening!")                       #[end]