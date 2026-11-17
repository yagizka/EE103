digit = str(input("Enter a 2 digit: "))
bit = int(digit)
binary_digit = ''
if bit == 0:
    binary_digit = '0'
else:
    while bit > 0:
        remainder = bit % 2
        binary_digit = str(remainder) + binary_digit
        bit = bit // 2
print(binary_digit)

