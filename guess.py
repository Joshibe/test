import random

checker = random.choice(range(10))

counter = 5
for num in range(counter):
    user_input = int(input("Guess A Number"))
    if user_input == checker:
        print("Correct Guess")
        break
    elif user_input < checker:
        print("It is Lower" + str(user_input))
        continue
    else:
        print("It is Higher" + str(user_input))
        continue

print(checker)

