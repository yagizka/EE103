cube = int(input("Enter a positive integer: "))
found = False
for guess in range(cube):
    if guess**3 == cube:
        found = True
        break
if found:
    print(f"Cube root of {cube} is {guess}")
else:
    print(f"{cube} is not a perfect cube")

