num = float(input("Enter a number to find its square root: "))
if num < 0:
    abs_num = abs(num)
    print(f"Did you mean: {abs_num}?")
    num = abs_num

epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001
while abs(guess**2 - num) >= epsilon:
    guess += increment
    num_guesses += 1
    if num_guesses % 1000 == 0 and guess <= num:
        print(f"Current guess: {guess}")
print(f"Number of guesses: {num_guesses}")
print(f"Approximate square root of {num}: {guess}")