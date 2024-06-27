from random import seed
from random import randint
max_guess = 1
min_guess = 100
guess = None
correct_number = randint(1,100)

print("="*28)
print("=Customizable Guessing Game=")
print("="*28)
print("\n")

print("Default game settings: Unlimited guesses from 1 to 100 with randomized correct number.\n")
default_game = input("Use default game settings? (y/n): ")
print("\n")

if default_game.lower() == 'y':
    while guess != correct_number:
        guess = int(input(f"Enter a number between {min_guess} and {max_guess}: "))
        if guess != correct_number:
            print(f"{guess} is wrong try again!")
            if guess > correct_number:
                print("Try lower.")
            else:
                print("Try higher.")
        else:
            break;

else:
    guesses = 0
    guess_limit = int(input("Max allowed guesses: "))
    min_guess = int(input("Lowest number: "))
    max_guess = int(input("Highest number: "))
    randomized_correct_number = input("Generate random correct number? (y/n): ")
    if randomized_correct_number.lower() == 'y':
        correct_number = randint(min_guess,max_guess)
    else:
        correct_number = int(input("Correct number: "))

    while guesses < guess_limit:
        guess = int(input(f"Enter a number between {min_guess} and {max_guess}: "))
        guesses+=1
        if guess != correct_number:
            print(f"{guess} is wrong try again!")
            if guess > correct_number:
                print("Try lower.")
            else:
                print("Try higher.")
        else:
            break

if guess != correct_number:
    print(f"You loose! The correct number was {correct_number} and you guessed {guess}!")
else:
    print(f"You win! Your guess {guess} is the same as the correct number of {correct_number}")
