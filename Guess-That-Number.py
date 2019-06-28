import random

random_num = random.randint(1, 20)
play_again = ""

print("Let's play Guess That Number!")

while True:
    user_guess = input("Think of a number between 1 and 20: ")
    user_guess = int(user_guess)

    while not 20 > user_guess > 0:
        print("The number should be between 1 and 20.")
        user_guess = int(input("Please enter a new number: "))

    if user_guess == random_num:
        play_again = input("Perfect, You guessed correctly! Play again? (y/n): ")

    if user_guess < random_num:
        print("Your guess is too low! Please enter a bigger number")

    elif user_guess > random_num:
        print("Your guess is too high! Please enter a smaller number: ")

    if play_again == "y":
        random_num = random.randint(1, 20)
        continue
    elif play_again == "n":
        break
