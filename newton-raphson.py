import secret_data
epsilon = 0.01
guess = secret_data.secret_number / 2  # Initial guess
guess_count = 0
while abs(guess**2 - secret_data.secret_number) >= epsilon:
    guess = (guess + secret_data.secret_number / guess) / 2  # Newton-Raphson formula
    guess_count += 1
print(f"Approximate square root of {secret_data.secret_number}: {guess}")
print(f"Number of guesses: {guess_count}")