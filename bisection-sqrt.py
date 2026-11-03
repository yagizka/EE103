root_num = int(input("Enter a number to find the square root of: "))
epsilon = 0.01
num_guesses = 0
increment = 0.0001
guess = 0.0
if root_num < 0:
    abs_root_num = abs(root_num)
    print(f"Did you mean: {abs_root_num}?")
    root_num = abs_root_num
elif root_num == 0:
    print(f"The square root of 0 is 0.")
else:
    while abs(guess**2 - root_num) >= epsilon:
        guess += increment
        num_guesses += 1
        if num_guesses % 1000 == 0 and guess <= root_num:
            print(f"Current guess: {guess}")
    print(f"Number of guesses: {num_guesses}")
    print(f"Approximate square root of {root_num}: {guess}")
if abs(guess**2 - root_num) < epsilon:
    print("result is good enough")
else:
    print("result is NOT good enough")



