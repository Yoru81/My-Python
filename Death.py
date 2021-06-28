import random

while True:
    target = input("Who do you want to kill?(Enter name): ")
    typeofdeath = input("How do you want " + target + " to die?(Painful , Peaceful , Natural): ")

    if typeofdeath.upper() == "PAINFUL":
        painfuldeath = [" Died by falling  into magma! " , " Died by being eaten by the most monsterous DEMON! "]
        print(target + random.choice(painfuldeath))
    elif typeofdeath.upper() == "PEACEFUL":
        peacefuldeath = [" Was Chilling in the cool breeze out in his patio, and just passed away as the wind went by." , " Ate a medicine which gave him/her death with no pain. "]
        print(target + random.choice(peacefuldeath))
    elif typeofdeath.upper() == "NATURAL":
        naturaldeath = " Just turned 100!(Happy Birthday!)The next second, He passed away due to his age. "
        print(target + naturaldeath)
