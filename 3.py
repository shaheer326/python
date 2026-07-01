a = 5
print("type of a:", type(a))

b = 3.5
print("type of b:", type(b))

c = "hello"
print("type of c:", type(c))

d = True
print("type of d:", type(d))

name = "penguin"
age = 15
is_student = True
weight = 60.5

print("name:", name)
print("data type of name:", type(name))

print("age:", age)
print("data type of age:", type(age))

print("is_student:", is_student)
print("data type of is_student:", type(is_student))

print("weight:", weight)
print("data type of weight:", type(weight))

print("\n after type casting...")
age = str(age)
print(age)
print("data type of age after casting:", type(age))

weight = int(weight)
print(weight)
print("data type of weight after casting:", type(weight))

text = str(input("enter your text: "))

revtext = text[::-1]
text = revtext

print("the reversed text is:")
print(text)