year = int(input("Enter a year: "))
year_sum = 0
for i in range(len(str(year))):
    year_sum += int(str(year)[i])
year_sum_2 = year_sum / len(str(year))
print(f"Sum of the digits in {year}: {year_sum}")
print(f"Average of the digits in {year}: {year_sum_2}")
    