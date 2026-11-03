k = int(input("Please enter a number for k: "))
epsilon = 0.01
guess = k / 2.0
while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k) / (2 * guess))
print(f"The square root of {k} is approximately {guess}.")