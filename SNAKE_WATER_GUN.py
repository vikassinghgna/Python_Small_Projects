import random

choices = ["s", "w", "g"]
score = 0
rounds = 5

def snake_water_gun(user, comp):
    if user == comp:
        print("It's a tie!")
        return 0
    elif (user == "s" and comp == "w") or \
         (user == "w" and comp == "g") or \
         (user == "g" and comp == "s"):
        print("You won this round!")
        return 1
    else:
        print("Computer won this round!")
        return 0

print("Welcome to Snake Water Gun Game!")
print("Enter your choice: s for Snake, w for Water, g for Gun")

for i in range(1, rounds + 1):
    print(f"\nRound {i}")
    user_input = input("Your choice (s/w/g): ")
    
    if user_input not in choices:
        print("Invalid input! Skipping this round.")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    score += snake_water_gun(user_input, computer_choice)

print(f"\nGame Over! Your total score out of {rounds}: {score}")



