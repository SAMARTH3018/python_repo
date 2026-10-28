n = int(input("Enter a number: "))

for i in range(1, 21):
    product = n * i
    if product % 2 == 0:
        print(n, "x", i, "=", product, "Even")
    else:
        print(n, "x", i, "=", product, "Odd")
