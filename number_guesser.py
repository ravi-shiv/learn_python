import random

top_of_range = input("Type a number: ")                          #taking the input frm user

if top_of_range.isdigit():                                       #checking the number is a digit   
    top_of_range = int(top_of_range)                             # converting teh user provided value to int data type.   

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')                     #else condition where the entered number is not digit. 
    quit()

random_number = random.randint(0, top_of_range)                   #using randint to convert value inside braces to int data type
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")
