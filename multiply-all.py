start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))
result_for = 1
result_while = 1
for i in range(start_num, end_num + 1):
    result_for *= i
while start_num <= end_num:
      result_while *= start_num
      start_num += 1
if result_for == result_while:
     print("Results are the same")
else:
        print("Results are different")