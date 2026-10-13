num = int(input("Enter a number for factorial: "))
result = 1
i = 1
while i <= num:
    result *= i
    i += 1
print(f"Factorial of {num} is {result}")