# Count digits in a positive integer
n = int(input("Enter a positive integer: "))
if n == 0:
    count = 1
else:
    count = 0
    n = abs(n)
    while n > 0:
        n //= 10
        count += 1
print("Digit count:", count)
