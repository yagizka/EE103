num = int(input("Enter a number: "))
total_sum = 0
for i in range(1, num + 1):
    total_sum += i
sum_gauss = num * (num + 1) / 2
print(f"Loop sum: {total_sum}, Gauss sum: {sum_gauss}")

if total_sum == sum_gauss:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")