def sqrt_guess_check(x):
    guess= 0
    while guess**2 < x:
        guess += 1
    if guess**2 == x:
        return guess
    return None

def sqrt_approximation(x, epsilon = 0.01, step = 0.0001):
    guess = 0.0
    while abs(guess**2 - x) >= epsilon and guess**2 <= x:
        guess += step
    return guess

def sqrt_bisection(x, epsilon = 0.01):
    low = 0
    high = max(1.0, x)
    guess = (high + low) / 2.0
    while abs(guess**2 - x) >= epsilon:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0
    return guess

print(sqrt_guess_check(64), sqrt_approximation(87), sqrt_bisection(98))

def is_even_or_odd(x):
    if type(x) != int:
        return None
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even_or_odd(5), is_even_or_odd(6), is_even_or_odd(7.5))

is_even_or_odd_alias = is_even_or_odd
print(is_even_or_odd_alias(7), is_even_or_odd(7), is_even_or_odd_alias(8), is_even_or_odd(8))
print(is_even_or_odd is is_even_or_odd_alias)