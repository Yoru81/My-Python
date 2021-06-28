while True:   
    Currency = float(input("Enter Currency value: "))
    unit = input("$(D) or £(P): ")
    if unit.upper() == "D":
        converted = (Currency * 0.7)
        print("Currency value in Pounds: " + str(converted))
    else:
        converted = (Currency * 1.4)
        print("Currency value in Dollars: " + str(converted))

    print()
    
