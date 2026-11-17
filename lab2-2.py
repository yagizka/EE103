number = 330206016
num = str(330206016)
num_lenght = len(num)
iteration_counter = 0
lower_bound = 10 ** int(len(num) / 2)
while lower_bound**2 <= 330206016:
    lower_bound += 1
    iteration_counter += 1
upper_bound = lower_bound**2
low_bound = (lower_bound - 1)**2
if abs(low_bound - 330206016) < abs(upper_bound -330206016):
     print(low_bound)
else:
    print(upper_bound)


    

