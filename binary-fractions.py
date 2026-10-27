num = float(input("Enter an integer for binary: "))
int_num = int(num)
num2 = num - int_num
bin_num = ''
binary_fraction = "0."
if int_num == 0:
    bin_num = '0'
else:
    while int_num > 0:
        remainder = int_num % 2
        bin_num = str(remainder) + bin_num
        int_num = int_num // 2
if num2 == 0:
    binary_fraction = ''
else:
    factor = 0.5
    while num2 > 0 and len(binary_fraction) < 20:
        num2 *= 2
        bit = int(num2)
        binary_fraction += str(bit)
        num2 -= bit
        factor /= 2
print(f"Binary representation: {bin_num}{binary_fraction}")