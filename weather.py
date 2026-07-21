weather = input("Enter the weather (rainy / sunny): ").strip().lower()

if weather == "rainy":
    print("Take an umbrela it might get wet outside")
elif weather == "sunny":
    print("Take sun glases you might need them")
else:
    print("Please select between sunny or rainy")