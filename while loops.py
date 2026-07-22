total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to finish!\n")

completed_count = 0
chore_num = 1

while chore_num <= total_chores:
    if chore_num == 1: next_chore = "make your bed"
    elif chore_num == 2: next_chore = "feed the pet"
    elif chore_num == 3: next_chore = "take out the trash"
    else: next_chore = "wash the dishes"

    answer = input(f"have you finished: {next_chore}? (yes/no): ")

    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("great job! chore complete")
    else:
        print("okay, finish it and check again!")

print("chores remaning: ", total_chores - completed_count)
print()

print("=====ALL CHORES COMPLETE!=====")
print("Great work finishing your entire checklist today!\n")

print("now let's safely peek at an infinite loop...")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("this condition never changes, so this would run forever")
    safety_counter += 1
    if safety_counter == 3:
        print("stopping here on perpose - a real infinite loop never stops on its own")
        break

print("\n====CHORE LIST SUMMARY====")
print("chores assigned today: ", original_count)
print("chores completed: ", completed_count)
print("chores left: ", total_chores - completed_count)
print("============================")