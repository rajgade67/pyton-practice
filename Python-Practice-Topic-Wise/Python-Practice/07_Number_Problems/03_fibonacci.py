# Print the first 7 Fibonacci numbers
a, b = 0, 1
for _ in range(7):
    print(a, end=" ")
    a, b = b, a + b
print()
