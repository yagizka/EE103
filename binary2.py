f = 0.375
binary_fraction = "0."

for _ in range(5):  
    f *= 2
    bit = int(f)
    binary_fraction += str(bit)
    f -= bit
    if f == 0:
        break

print(f"Binary fraction: {binary_fraction}")