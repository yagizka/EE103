
import week7_def


def count_even(func, n):
    count = 0
    for i in range(n):
        if func(i) == "Even":
            count += 1
    return count
print(count_even(week7_def.is_even_or_odd, 5))   # 3  (0, 2, 4)
