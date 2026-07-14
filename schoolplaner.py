print("=== Smart School Planner ===")
print("Answer 3 quick questions and i will plan your day! \n")

day = input("What is it? (Monday to sunday): ").strip().capitalize()
weather = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
homework = input("Is your homework done? (Yes / No): ").strip().lower()

print()
print(f"=== Your plan for {day} ===")
print("-" * 35)

if day in ("Saturday , Sunday"):
    print("Day type:    Weekend - Enjoy your free time!")
elif day == ("Monday"):
    print("Day type:    First day of the week. Pack your weekly planner.")
elif day in ("Tuesday , wednesday , friday"):
    print("Day type:    Regular school day. Stay focused!")
else:
    print("Day type:    Not recognised. Please check the spelling.")

if weather == "sunny" and homework == "yes":
    print("Afer school:     Head to the park - Great weather and home work is done!")

if weather == "rainy" or "cloudy":
    print("Weather Tip:     It may get wet outside.")

if not (homework == "yes"):
    print("Homework:    Not done - finish it before going out!")

if weather == "rainy" and not homework == "yes":
    print("Best Plan:   Stay in, finish your homework, then watch your favorite show.")
elif weather == "sunny" and homework == "yes" and not (day in("Saturday" , "Sunday")):
    print("Best Plan:   All set for a great school day - you are prepaired")
elif day in("Saturday" , "Sunday") and weather == "sunny":
    print("Bet plan:    Perfect weekend weather - head outside and have FUN!")
else:
    print("Best plan:   Take one step at a time - You got this")

print()
print("Plan complete! Have a wonderful day!")