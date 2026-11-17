number = int(input("Enter n: "))
total = 0.0
for i in range(number):
    total += 0.1
print("Total:", total)
print("Equal:", total == number / 10)
print("Close enough:", abs(total - number / 10) < 1e-9) 
    
       
            