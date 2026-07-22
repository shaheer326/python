n = int(input("Enter a number: "))

if not n == "":
    p = int(input("Enter the number's power: "))
    if not p == "":
        output = n ** p
        print("the output is: ", output)
    else:
        print("enter a valid number")
else:
    print("enter a valid number")