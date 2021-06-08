while True:    
    first_number = int(input("Enter First Number: "))
    print("+ = Addition\n- = Subtraction\n/ = Division\n* = Multiplication\n// = Integer Division\n% = Reminder only\n0 = exit")
    character = input("Enter a character: ")
    if character == "0":
        break
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
        print("\nENTER THE RIGHT CHARACTER\n")
    
        

    
