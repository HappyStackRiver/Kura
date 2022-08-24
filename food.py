DATE_ATENDEE_1="Rey"
DATE_ATENDEE_2="Areli"
MENU={"Drinks": ["Water", "Soda", "Wine"], "Dinner": ["Fettucini", "Lobster", "Gnocchi"], "Dessert": ["Tiramisu", "Cheesecake", "Gelato"]}
RESTAURANT_NAME="Casa de Happy"
FEELINGS=["Sad", "Happy", "Annoyed", "Scared"]

#choice checks
def beverageError():
    print("Sorry, that was not an option")
    print("Please decide again")
    beverageChoice()

def beverageChoice():
    print("Please select a beverage")
    BEVERAGE_CHOICE=input()
    if (BEVERAGE_CHOICE != "Water" and BEVERAGE_CHOICE != "Soda" and BEVERAGE_CHOICE != "Wine"):
        beverageError()
    else:
        return BEVERAGE_CHOICE

def dinnerError():
    print("Sorry, that was not an option")
    print("Please decide again")
    dinnerChoice()

def dinnerChoice():
    print("Please select a dinner")
    DINNER_CHOICE=input()
    if (DINNER_CHOICE != "Fettucini" and DINNER_CHOICE != "Lobster" and DINNER_CHOICE != "Gnocchi"):
        dinnerError()
    else:
        return DINNER_CHOICE

def dessertError():
    print("Sorry, that was not an option")
    print("Please decide again")
    dessertChoice()

def dessertChoice():
    print("Please select a dessert")
    DESSERT_CHOICE=input()
    if (DESSERT_CHOICE != "Tiramisu" and DESSERT_CHOICE != "Cheesecake" and DESSERT_CHOICE != "Gelato"):
        dessertError()
    else:
        return DESSERT_CHOICE

def choiceError():
    print("Sorry, that was not an option")
    print("Please decide again")
    choiceTent()

def choiceTent():
    print("Please select 1-4")
    TENT_INPUT=input("I pick number: ")
    print(TENT_INPUT)

    if int(TENT_INPUT) == 1:

        print("Oh that sucks! Let me just cover the bill since your boyfriend has aproximately 5 minutes before he dies")
        print("Have a good day!")
        exit()

    if int(TENT_INPUT) == 2:
        print("Well good thing that you now are part god. You still have to pay for the food tho.")

    if int(TENT_INPUT) == 3:
        print("Well I am also annoyed by you and him. Good thing I'm hungry too! Run.")
        print("---Rey was made into sausages and you wash dishes now---")
        exit()

    if int(TENT_INPUT) == 4:
        print("Well that was a good answer. I'll change my form back into normal. Pay for the food now!")

    if int(TENT_INPUT) != 1 and int(TENT_INPUT) != 2 and int(TENT_INPUT) != 3 and int(TENT_INPUT) != 4):
        choiceError()
        


#introductory print stuff
print("Hello! Welcome to",RESTAURANT_NAME)
print("I have confirmed reservations for you Mister", DATE_ATENDEE_1)
print("Ah, I see you are eating with us again", DATE_ATENDEE_2)
print("As you know, there is still that policy of having to tell us how much you're planning on spending")
print("Please do tell what budget you have tonight sir?")
print("-------------------")
BUDGET=input("I hate that this restaurant does this...My budget is $")
print("-------------------")
print("I do apologize. So it's", BUDGET)
print("Here is the menu!")

#for loop for printing menu
for key, value in MENU.items():
    print("{}:{}".format(key,MENU[key]))

#get user input for each key
REY_DRINK=beverageChoice()
print(REY_DRINK,"it is then!")
print("What about you", DATE_ATENDEE_2)
ARELI_DRINK=beverageChoice()
print("Great Choice!")

REY_DINNER=dinnerChoice()
print(REY_DINNER,"it is then!")
print("What about you", DATE_ATENDEE_2)
ARELI_DINNER=dinnerChoice()
print("Great Choice!")

REY_DESSERT=dessertChoice()
print(REY_DESSERT,"it is then!")
print("What about you", DATE_ATENDEE_2)
ARELI_DESSERT=dessertChoice()
print("Great Choice!")

print("EAT UP!!!")
print("----------------------------------")
print("A FEW MINUTES LATERRRR")
print("Rey: This place low key kinda bunk")
print("Areli: Yeah, but the food is fire!")
print("Rey: Why do we come here tho? The food is good but the waiter is weird and he deadass has a third eyeball with tentacle teeth")
print("Areli: ....")
print("Areli: I think he spiked your drink again babe")
print("Rey: Ah, I remember. That's why I come here")
print("----------------------------------")
print("HOW WAS THE FOOD HAPPY? DID YOU ENJOY IT?")
print("----------------------------------")
print("Yes. I remember you like to do illegal activities for the poor")
print("----------------------------------")
print("Well, I'm an interdimensional being not bounds by the rules and logic.")
print("Areli: I hate you and everything you stand for tentacle face")
print("----------------------------------")
print("Well, I'm going to give you 4 options to tell me how you feel about today.")
print("Option 1. Sad")
print("Option 2. Happy")
print("Option 3. Annoyed")
print("Option 4. Scared")
print("So Areli, how do you feel? He's clearly out of it")
choiceTent()
print("Alright so since you made it this far do some math")
print("Kidding, this restaurant does not exist! Casa de Happy was a dream. Dream food doesn't cost money silly")
print("Alright Areli, you ordered the following", ARELI_DRINK, ARELI_DINNER, ARELI_DESSERT)
print("Here Rey, you ordered the following", REY_DRINK, REY_DINNER, REY_DESSERT)
exit()