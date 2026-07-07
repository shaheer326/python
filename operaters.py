t1 = 98
t2 = 99
t3 = 96
t4 = 93
t5 = 95

sum = t1 + t2 + t3 + t4 + t5
print("the sum of the marks is:", sum)

average = sum/5
print("the average of the marks is:", average)

Amount = int(input("enter the amount you want to withdraw: "))

note_1 = Amount // 100
note_2 = (Amount % 100) // 50
note_3 = (Amount % 100) % 50 // 10

print("the number of 100 rupee", note_1)
print("the number of 50 rupee", note_2)
print("the number of 10 rupee", note_3)

print("enter obtained marks:")
math = int(input("math: "))
english = int(input("english: "))
science = int(input("science: "))
history = int(input("history: "))

sum = math + english + science + history
print("the sum of the marks is:", sum)

perc = (sum / 400) * 100
print(end="percentage marks: ")
print(perc)