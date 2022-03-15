import random

user_wins = 0
computer_wins = 0

options = ["heads", "tails"]

print("Lets toss the coin!!!!")

while True:
 
    user_input = input("Heads/Tails or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    tossed_coin = random.randint(0, 1)
    computer_pick = options[tossed_coin]
    print("Computer picked", computer_pick + ".")

    if user_input == "heads" and computer_pick == "tails":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
