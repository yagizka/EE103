import secret_data
guess = 0
epsilon = 0.01
increment = 0.0001
guess_count = 0
if secret_data.secret_number < 0:
    abs_num = abs(secret_data.secret_number)
    print(f"Did you mean: {abs_num}?")
    secret_data.secret_number = abs_num
else:
    while abs(guess**2 - secret_data.secret_number) >= epsilon:
        guess += increment
        guess_count += 1
    print(f"Approximate square root of {secret_data.secret_number}: {guess}")
    print(f"Number of guesses: {guess_count}")
