while True:
    Temperature = int(input("Enter Temperature: "))
    unit = input("C or F: ")
    if unit.upper() == "C":
        converted = (Temperature * 9/5) + 32
        print("Temperature in Farhenheit: " + str(converted))
    else:
        converted = (Temperature -32) * 5/9
        print("Temperature in Celcius: " + str(converted ))
