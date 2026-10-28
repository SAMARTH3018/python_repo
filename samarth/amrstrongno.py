n = int(input("Enter a three-digit number: "))

original = n
total = 0

if n < 100 or n > 999:
    print("Enter a three-digit number")
else:
    while n > 0:
        digit = n % 10
        total += digit ** 3
        n = n // 10

    if total == original:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")