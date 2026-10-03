print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")
print("\nOptions:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
numberOption = input("Your choice: ")
if numberOption == "1":
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    numinput = input("Your choice: ")
    if numinput == "1":
        meters = float(input("Insert meters: "))
        kilometers = meters / 1000
        print(f"{meters} m is {kilometers} km")
    elif numinput == "2":
        kilometers = float(input("Insert kilometers: "))
        meters = kilometers * 1000
        print(f"{kilometers} km is {meters} m")
    elif numinput == "0":
            print("your choice is 0:")
    elif numinput == "2":
      print("\nWeight options:")
      print("1 - Grams to kilograms")
      print("2 - Kilograms to grams")
      print("0 - Exit")
    Input2 = input("Your choice: ")
    if Input2 == "1":
        grams = float(input("Insert grams: "))
        pounds = grams * 0.002205
        print(f"{grams} g is {pounds} lb")
    elif Input2 == "2":
        pounds = float(input("Insert pounds: "))
        grams = pounds * 453.6
        print(f"{pounds} lb is {grams} g")
    else:
        print("unknown option.")    
print("Exiting...")

print("Program ending.")
