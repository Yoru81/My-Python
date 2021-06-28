import random

win = False
points = 1
a = random.randint(1, 100)

while (win == False):
    input_num = int(input("Guess the number: "))

    if input_num > a:
        print("You guess is higer than the number. Try Again")
        points += 1
    elif input_num < a:
        print("You guess is lesser than the number. Try Again")
        points += 1
    else:
        win = True
        
print("\nCongratulations!!!! You guessed the right number.")
print("Number of tries:", points)