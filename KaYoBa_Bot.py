while True:
    enter_command = input("Enter a command (Type Help to see commands): ")

    if enter_command.upper() == "CALCULATE":
        first_number = int(input("Enter First Number: "))
        print("+ = Addition\n- = Subtraction\n/ = Division\n* = Multiplication\n// = Integer Division\n% = Reminder only\n")
        character = input("Enter a character: ")
        second_number = int(input("Enter Second Number: "))


        
        if character == "+":
            added = (first_number + second_number)
            print(added)
        elif character == "-":
            subtracted = (first_number - second_number)
            print(subtracted)
        elif character =="/":
            if second_number == 0:
                print("\nDivision by 0 is not possible, try again\n")
            else:
                divided = (first_number / second_number)
                print(divided)
        elif character == "*":
            multiplied = (first_number * second_number)
            print(multiplied)
        elif character == "//":
            if second_number == 0:
                print("\nDivision by 0 is not possible, try again\n")
            else:
                integer_divided = (first_number // second_number)
                print(integer_divided)
        elif character == "%":
            if second_number == 0:
                print("\nDivision by 0 is not possible, try again\n")
            else:
                reminder_only = (first_number % second_number)
                print(reminder_only)
        else:
            print("\nERROR.ENTER THE RIGHT CHARACTER\n")  


    elif enter_command.upper() == "JOKE":
        import random
        joke_list = [" What’s the best thing about Switzerland? I don’t know, but the flag is a big plus." , " What did the traffic light say to the other? Stop looking at me, I'm changing! " , "Why do we tell actors to break a leg? Because every play has a cast. " , "A bear walks into a bar and says, Give me a whiskey and … cola. “Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.” " ]
        print(random.choice(joke_list))

    elif enter_command.upper() == "QUOTE":
        print("\n\"If you cannot do great things, do small things in a great way\"\n")

    elif enter_command.upper() == "PIG":
        print("""                        ████████████                                                            
            ██████  ██████░░░░░░░░░░░░██████    ██████                                            
            ██░░░░████░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░████                                        
        ██░░░░██▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒██░░░░░░▒▒██                                      
        ██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░██                                    
        ██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░████████████                          
        ██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░██░░░░░░░░▒▒██████                    
        ██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░░░░████                      Hey
        ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░░░░░░░░██                          Hiya
        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓████▒▒░░░░░░░░░░░░░░░░░░░░▓▓██                             Doin
        ██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░▒▒██      ████ 
    ██░░░░░░██░░░░██████░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██  ██░░██ 
    ██░░░░░░▓▓████░░░░░░████░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██  ██░░██ 
    ██░░░░░░██░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██     OOPS! I mean OINK! OINK!
    ██░░░░░░██░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██  
    ██░░░░░░██░░░░██░░░░░░██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
    ██░░░░░░██░░░░██░░░░░░██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
    ██░░░░░░██░░░░░░░░░░░░░░░░░░██░░████░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
    ██░░░░░░▒▒████░░░░░░░░░░████░░░░██▒▒██░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
    ██░░░░░░▒▒▒▒██▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓██░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
    ██░░░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓██░░  ░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
        ██░░░░░░░░      ░░████████████░░      ░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
        ██░░░░░░        ░░░░░░░░░░░░          ░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
            ██░░░░░░                            ░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██      
            ████░░░░                          ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██      
                ████████                ██████░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██      
                        ████████████████░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██        
                            ██░░░░░░  ░░        ░░░░░░░░░░░░░░██            ██░░░░░░░░░░░░██        
                            ██░░░░░░██          ░░░░░░░░░░░░░░██            ██░░░░░░░░░░██          
                            ██░░░░░░████████████░░░░░░░░░░░░████████████████░░░░░░░░░░██          
                            ██░░░░░░░░██        ██░░░░░░░░██                ██░░░░░░██            
                                ██▓▓▓▓██            ██▓▓▓▓██                  ██▓▓▓▓██              
                                ████░░              ████                      ████                
                                                                                    """)

    elif enter_command.upper() == "HELP":
        print("""\nCommands: 
            Help - Shows all commands
            0    - Exit Bot
            Mood - Asks you your mood
            Pig  - Draws a pig
            Calculate - Calculates 2 numbers
            Joke - Tells a joke
            Quote - Tells a quote
            Ping - See what it says  =)
            Dev name - See who developed this bot
            Naruto - Draws Naruto!
            Senlen - Compare length of 2 sentences
            FWS - Find a word in the given sentence
            Tempcon - Convert temperature C-F or F-C
            Currcon - Convert Dollars to Pounds and Pounds to Dollars
            OE - Tells if entered number is Odd or Even
            Kill - Kills a person
            GNG - Guessing number game
            Compare - Compares the 2 enterd numbers.
            Anime Ranking - Gives the top 5 anime.
            Chr Counter - Tells you all the characters in the given sentence / word.\n""")

    elif enter_command.upper() == "CHR COUNTER":
        up = low = dig = sp = spl = 0
        enter_string = input("Enter a string: ")

        for character in enter_string:
            if character.isupper():
                up += 1
            elif character.islower():
                low += 1
            elif character.isdigit():
                dig += 1
            elif character.isspace():
                sp += 1
            else:
                spl += 1
        
        print("\nNumber of Upper Characters: ", up)  
        print("Number of Lower Characters: " , low)
        print("Number of numbers(lel): " , dig) 
        print("Number of spaces: " , sp)
        print("Number of Special Characters: " , spl)

    elif enter_command.upper() == "ANIME RANKING":
        print("#1 Fullmetal Alchemist Brotherhood\n#2 Demon Slayer\n#3 Naruto\n#4 One Piece\n#5 Attack on Titan")

    elif enter_command.upper() == "COMPARE":
        number_1 = input("Enter first number: ")
        number_2 = input("Enter second number: ")

        if number_1 > number_2:
            print( number_1 + " is greater than " + number_2)

        elif number_1 < number_2:
            print( number_1 + " is lesser than " + number_2)

        else:
            print("Both given numbers are equal.")

    elif enter_command.upper() == "GOOD MORNING":
        print("\nGood Morning. Have a nice day!\n")

    elif enter_command.upper() == "GOOD NIGHT":
        print("Have a Good Night of sleep!")

    elif enter_command.upper() == "GNG":
        import random

        win = False
        points = 1
        a = random.randint(1, 100)

        while (win == False):
            input_num = int(input("Guess the number: "))

            if input_num > a:
                print("You guessed is higer than the number. Try Again")
                points += 1

            elif input_num < a:
                print("You guessed is lesser than the number. Try Again")
                points += 1

            else:
                win = True
        
        print("\nCongratulations!!!! You guessed the right number.")
        print("Number of tries:", points)


    elif enter_command.upper() == "KILL":
        import random

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


    elif enter_command.upper() == "OE":
        n = int(input("Enter a number: "))
        if (n % 2 == 0):
            print("Even")

        else:
            print("Odd")

    elif enter_command.upper() == "CURRCON":
        Currency = float(input("Enter Currency value: "))
        unit = input("$(D) or £(P): ")
        if unit.upper() == "D":
           converted = (Currency * 0.7)
           print("Currency value in Pounds: " + str(converted))
        else:
             converted = (Currency * 1.4)
             print("Currency value in Dollars: " + str(converted))


    elif enter_command.upper() == "TEMPCON":
        Temperature = int(input("Enter Temperature: "))
        unit = input("C or F: ")

        if unit.upper() == "C":
           converted = (Temperature * 9/5) + 32
           print("Temperature in Farhenheit: " + str(converted))
        else:
             converted = (Temperature -32) * 5/9
             print("Temperature in Celcius: " + str(converted ))

    elif enter_command.upper() == "SENLEN":
        first_sen = input("Enter first sentence[Minimum 5 words]: ")
        second_sen = input("Enter second sentence[Minimum 5 words]: ")

        first_senlen = len(first_sen)
        second_senlen = len(second_sen)

        if first_senlen > second_senlen:
           print("First Sentence is longer than the second sentence.")

        elif first_senlen == second_senlen:
             print("Length of both sentences are equal.")

        else:
             print("Second sentence is longer than the first sentence.")


    elif enter_command.upper() == "MOOD":
        mood = input("How is your mood rn(Sad or Happy)? ")
        
        if mood.upper() == "SAD":
            print("""\nME: Hugs you
YOU: Feel better\n""")

        elif mood.upper() == "HAPPY":
            print("\nI'm happy to hear that your happy.\n")
            
        else:
            print("\nERROR. If your happy enter happy.If your sad enter sad.\n")


    elif enter_command.upper() == "NARUTO":
        print("""                                                                            
                                      ▓▓▓▓▓▓  ▓▓▓▓▓▓                                
                                      ▓▓  ░░▓▓▓▓  ▓▓▓▓▓▓                            
                                ▓▓▓▓▓▓▓▓░░  ░░▓▓░░░░▓▓▓▓  ▓▓                        
                              ▒▒▓▓░░  ▓▓░░░░░░░░░░░░▓▓░░░░▓▓                        
                                  ▒▒░░  ░░░░░░░░░░░░░░░░▓▓▓▓▒▒                      
                                  ▓▓░░░░░░░░░░░░░░░░░░░░▓▓░░▓▓                      
                ██████████    ▒▒▓▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓                      
            ██████      ██████    ▓▓▓▓▓▓▓▓▓▓▓▓▒▒    ▒▒▒▒▒▒▓▓▓▓                      
          ████              ████████▓▓▓▓▓▓▓▓▓▓▒▒    ▒▒  ▒▒▓▓                        
        ████                  ██████░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                          ██████████░░  ░░░░░░██░░░░░░████                          
                    ██████████    ██░░░░░░░░░░▒▒░░░░░░▒▒██                          
              ██████████          ██░░░░░░░░░░░░░░░░░░░░██                          
        ██████████                  ████░░░░░░░░░░░░░░░░██    Watashi wa hokage ni naru!                      
      ██████                          ████░░░░░░▒▒▒▒░░██                            
    ████                              ██▓▓██░░░░░░░░██                              
  ████                          ████████▓▓▓▓████████                                
  ██                          ████▓▓▓▓▓▓████████▓▓██████                            
  ██                        ████▓▓▓▓▓▓▓▓▓▓██████▓▓██▓▓▓▓██                          
                          ▓▓████▓▓▓▓██▓▓▓▓▓▓▓▓██▓▓██▓▓██▓▓▓▓                        
                        ████████▓▓▓▓██▓▓▓▓▓▓▓▓██▓▓██▓▓██▓▓██                        
                      ██▓▓▓▓▓▓▓▓████████████████▓▓██████▓▓██                        
                      ██▓▓██▓▓▓▓████▒▒░░░░  ░░░░▓▓██▒▒██▓▓██                        
                    ██▓▓▓▓██████████▒▒  ░░░░    ▓▓██▒▒██▓▓████                      
                    ██▓▓▓▓▓▓████  ██▒▒░░    ░░░░▓▓██▒▒▒▒██████                      
                  ██▓▓▓▓▓▓▓▓██    ██▒▒░░░░      ▓▓██▒▒▒▒██▓▓██                      
                  ██▓▓▓▓▓▓▓▓██    ██▒▒░░░░░░░░░░░░▓▓██▒▒██▓▓██                      
                ██▓▓▓▓████▓▓██    ████▒▒░░    ░░░░▓▓██▒▒██▓▓▓▓██                    
                ██▓▓██░░░░██        ████████▓▓▓▓▓▓▓▓████████▓▓▓▓████                
                  ██░░░░████        ████████████████████████▓▓████░░████            
                ██░░░░░░░░██        ██▒▒░░░░░░░░░░░░░░░░████▓▓██░░░░░░░░██          
                ██░░░░░░░░░░██      ██░░    ░░░░░░░░░░░░░░░░████░░░░░░░░██          
                ██░░░░░░░░░░██      ██▒▒░░░░    ░░░░██░░░░░░████░░░░░░██            
                ██░░░░░░░░██      ██▒▒  ▒▒▒▒▒▒░░░░░░██░░░░░░░░████████              
                  ████████        ██████    ▒▒▒▒████░░████░░░░██                    
                                  ██    ████▒▒██  ████▒▒▒▒▒▒▒▒░░██                  
                                ██░░░░░░  ▒▒▒▒██    ██▒▒▒▒▒▒▒▒░░░░██                
                                ██░░░░░░▒▒▒▒██        ██▒▒▒▒▒▒▒▒░░██                
                              ██░░░░░░▒▒▒▒▒▒██        ██▒▒▒▒▒▒▒▒░░██                
                            ██░░░░░░░░▒▒▒▒██            ██▒▒▒▒▒▒▒▒░░██              
                            ██░░░░░░▒▒▒▒▒▒██            ██▒▒▒▒▒▒▒▒░░██              
                          ██░░░░░░▒▒▒▒▒▒██              ██▒▒▒▒▒▒░░░░██              
                        ██░░░░░░▒▒▒▒▒▒██                ██▒▒▒▒▒▒▒▒░░██              
                        ██░░░░░░▒▒▒▒▒▒██                ██▒▒▒▒▒▒▒▒░░██              
                          ██░░▒▒▒▒▒▒██                    ████████████              
                        ████████████                        ████████                
                        ██▓▓▓▓████                          ██▓▓▓▓██                
                      ████████████                        ██▓▓██████████            
                    ██▓▓▓▓▓▓▓▓██                          ██▓▓▓▓▓▓▓▓▓▓▓▓████        
                  ██▓▓▓▓▓▓▓▓▓▓██                          ██████▓▓▓▓▓▓░░░░░░██      
                ██▓▓░░░░░░░░████                                ██████████████      
                ██████████████                                                """) 
    
    elif enter_command.upper() == "PING":
        print("\nPONG!\n")

    elif enter_command.upper() == "DEV NAME":
        print("\n---- Developed this project\n")

    elif enter_command == "0":
        break

    else:
        print("""\nERROR.You have entered an invalid command. Type Help to see all commands.\n""")
     
     
