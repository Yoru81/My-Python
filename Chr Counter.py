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







    

