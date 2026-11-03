secret = int(input("Enter a secret page number between 1 and 148: "))
low = 1
high = 148
num_guesses = 0
while True:
    guess = (low + high) // 2
    num_guesses += 1
    if guess == secret:
        print(f"I FOUND IT AFTER {num_guesses} GUESSES! The secret page number is {guess}.")
        break
    elif guess < secret:
        low = low + 1
    else:
        high = high - 1

