import secret_data
guess = 0
guess_count = 0
while guess != secret_data.secret_year:
    guess += 1
    guess_count += 1
print(f"Secret year is: {secret_data.secret_year}")
print(f"Number of guesses: {guess_count}")