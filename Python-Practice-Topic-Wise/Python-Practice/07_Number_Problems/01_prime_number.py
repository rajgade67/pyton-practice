n = int(input("Enter a number: "))

if n < 2:
    print("It is not a prime number")
else:
    for divisor in range(2, n):
        if n % divisor == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
