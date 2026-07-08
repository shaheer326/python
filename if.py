num = 3
if num > 0:
    print("num is a positive number.")

num = -1
if num > 0:
    print("num is a positive number.")

actual_cost = float(input("Enter the actual cost of the item: "))
sale_amount = float(input("Enter the sale amount of the item: "))

if sale_amount > actual_cost:
    amount = sale_amount - actual_cost
    print("total profit = {0}".format(amount))

num = int(input("Enter a number: "))

if num > 15:
    print("The number is greater than 15.")
else:
    print("The number is not greater than 15.")


num = int(input("Enter a number: "))
if num%2==0:
    print("this is an even number")
else:
    print("this is an odd number")