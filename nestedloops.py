print("====ATM Cash Dispenser====\n")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_serverd = 0
total_dispensed = 0

serving = True
while serving:
    name = input("Please enter your name: ")
    ammount = int(input(f"Heloo {name}! Enter your withdrawal ammount: "))
    if ammount <= 0:
        print("invalid ammount, please enter a positive number.\n")
        continue

    print(f"\nDispensing {ammount} units for {name}: ")
    remaining = ammount
    idx = 1
    while idx <= 6:

        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        else: value = 1
        count = remaining // value
        if count > 0:
            print(f"   {count} x {value}-un")