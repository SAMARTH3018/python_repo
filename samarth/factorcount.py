n = int(input("Enter a positive integer: "))

count = 0

print("Factors:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        count += 1

print("\nTotal factors =", count)