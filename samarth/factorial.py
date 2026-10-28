n = int(input("Enter a non-negative integer: "))

fact = 1

if n < 0:
    print("Enter a non-negative integer")
else:
    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial =", fact)
    