std_num = str(input("Input student ID: "))
indi_digits = ''
sum_digits = ''
for char in std_num:
    indi_digits = char + "," + indi_digits
print(f"Individual Digits:  {indi_digits}")

