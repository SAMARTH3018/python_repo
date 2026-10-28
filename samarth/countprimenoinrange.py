start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0

for n in range(start, end + 1):
    prime = n > 1

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, end=" ")
        count += 1

print("\nTotal prime numbers =", count)