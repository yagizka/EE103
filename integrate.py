
from week8_recap import take_square

import pdb; pdb.set_trace()
def integrate(func, steps=1000):
    total_area = 0
    dx = 1 / steps
    for i in range(steps):
        x_i = (i + 0.5) * dx
        total_area += func(x_i) * dx
    return total_area
print("Value of integral: ",integrate(take_square))