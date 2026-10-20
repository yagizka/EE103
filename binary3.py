target = 0.1
f = target
binary_fraction = "0."
approx = 0.0
factor = 0.5

for _ in range(20):
    f *= 2
    bit = int(f)
    binary_fraction += str(bit)
    approx += bit * factor
    factor /= 2
    f -= bit
    
    if abs(approx - target) < 0.00001:
        break

print(f"Approximated binary for 0.1: {binary_fraction}")