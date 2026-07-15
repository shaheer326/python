print("==========================================")
print("|         Welcome to ride builder!       |")
print("==========================================")
print()

print("Step 1: Pick your vehicle")
print("  1 - bike")
print("  2 - car")
print()

choice = int(input("Enter 1 or 2: "))
print()

if choice == 1:
    print("Step 2: Pick your bike type")
    print("  1 - Scooty")
    print("  2 - Mountain Bike")
    print()

    bike_type = int(input("Enter 1 or 2: "))
    print()

    if bike_type == 1:
        print("You picked : Scooty")
        print("Top Speed  : 80km/h")
        print("Best for   : city roads")
    else:
        print("You picked : Mountain Bike")
        print("Top Speed  : 40km/h")
        print("Best for   : Off-road trails")

elif choice == 2:
    print("Step 2: Pick your Car type")
    print("  1 - Sedan")
    print("  2 - SUV")
    print()

    car_type = int(input("Enter 1 or 2: "))
    print()

    if car_type == 1:
        print("You picked : Sedan")
        print("Seats      : 5 passenger")
        print("Best for   : Family trips")
    else:
        print("You picked : SUV")
        print("Seats      : 7 passenger")
        print("Best for   : Off-road Adventures")

else:
    print("That was not a valid choice.")
    print("Please enter 1 for Bike and 2 for Car.")

print()
print("========================================")
print("|      Your Custom Ride is Ready!      |")
print("|         Enjoy the Journey!           |")
print("========================================")