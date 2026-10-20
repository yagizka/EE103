from secretnumber2 import secretNum
attempts = 0
while True:
    if attempts >= 5:
        print("You failed after 5 guesses!")
        break

    guess = int(input("Guess the number: "))
    attempts += 1

    if guess == secretNum:
        print("Correct!")
        break
    elif guess < secretNum:
        print("Too low!")
    else:
        print("Too high!")
while True:
        print("Oh! Noooooo...")