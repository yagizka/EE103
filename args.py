def mean(*args):
    tot = 0
    for a in args:
        tot += float(a)      # '3' -> 3.0
    return tot / len(args)
print("Mean: ", mean(1, 2, 3, 4, 5))
print("Mean: ", mean('1', '2', '3', '4', '5'))