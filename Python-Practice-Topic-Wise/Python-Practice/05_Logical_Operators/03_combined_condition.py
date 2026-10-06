n = int(input("Enter the number: "))

for val in range(1, n + 1):
    if (val % 2 == 0 or val % 3 == 0) and val % 6 != 0 and val > 10:
        print(val)
