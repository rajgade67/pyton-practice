num = int(input("Enter number: "))
total = 0

while num > 0:
    d = num % 10
    total += d
    num //= 10

print("Sum:", total)
