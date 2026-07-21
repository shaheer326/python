n = int(input("Enter the number whose sum you want to find: "))
sum = 0

for i in range(1, n+1):
    sum = sum+1
    print("\nSum =", sum)

string = input("Please enter your string: ")

string2 = ('')

for i in string:
    string2 = i + string2

print("\nThe Original String = ", string)
print("\nThe Reversed String = ", string2)

num = int(input("Enter the value of num: "))

print("numbers from {0} to {1} are: ".format(num,1))

for i in range(num,0,-1):
    print(i)