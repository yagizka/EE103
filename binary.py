num = 13
binary_result = ""

if num == 0:
    binary_result = "0"

while num > 0:
    remainder = num % 2
    binary_result = str(remainder) + binary_result
    num = num // 2

print(f"Binary representation: {binary_result}")