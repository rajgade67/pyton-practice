n = int(input("Enter the number: "))

for val in range(1, n + 1):
    if (val % 5 == 0 or val % 7 == 0) and (val % 35 != 0 and val > 20):
        print(val)
