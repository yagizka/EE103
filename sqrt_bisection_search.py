import secret_data
guess = 0
guess_count = 0
while guess != secret_data.secret_year:
    guess += 1
    guess_count += 1 
print(f"Found the secret year: {guess} in {guess_count} guesses.")