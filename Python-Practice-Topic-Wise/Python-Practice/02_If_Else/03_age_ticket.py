age = int(input("Enter age: "))

if age <= 12:
    print("Ticket price 100")
elif age <= 18:
    print("Ticket price 150")
elif age <= 59:
    print("Ticket price 200")
else:
    print("Ticket price 120")
