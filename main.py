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
        print("Exiting...")
    else:
        print("Unknown option.")

elif numberOption == "2":
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    weightInput = input("Your choice: ")
    if weightInput == "1":
        grams = float(input("Insert grams: "))
        pounds = round(grams / 453.6, 1)
        print(f"{grams} g is {pounds} lb")
    elif weightInput == "2":
        pounds = float(input("Insert pounds: "))
        grams = round(pounds * 453.6, 1)
        print(f"{pounds} lb is {grams} g")
    elif weightInput == "0":
        print("Exiting...")
    else:
        print("Unknown option.")

elif numberOption == "0":
    print("Exiting...")

else:
    print("Unknown option.")

print("Program ending.")