n = int(input("Enter a positive integer: "))

prime = n > 1

for i in range(2, n):
    if n % i == 0:
        prime = False
        break
if prime:
    print("Prime number")
else:
    print("Not a prime number")