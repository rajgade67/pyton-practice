# Reverse the digits of an integer
num = int(input("Enter an integer: "))
sign = -1 if num < 0 else 1
n = abs(num)
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10
print("Reverse:", sign * reverse)
