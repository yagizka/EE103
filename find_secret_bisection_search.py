import secret_data
low = 0
high = 2026
guess = (low + high) / 2
num_guesses = 0
while guess != secret_data.secret_year:
    num_guesses += 1
    if guess < secret_data.secret_year:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2
num_guesses += 1
print(f"Secret year is: {secret_data.secret_year}")
print(f"Number of guesses: {num_guesses}")