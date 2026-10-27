num = int(input("Enter an integer for binary: "))
bin_num = ''

if num == 0:
    bin_num = '0'
else:
    while num > 0:
        remainder = num % 2
        bin_num = str(remainder) + bin_num
        num = num // 2

print(f"Binary representation: {bin_num}")