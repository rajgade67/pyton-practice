n = int(input("Enter number: "))

for val in range(1, n + 1):
    if val % 5 == 0 or val % 7 == 0:
        print(val)
