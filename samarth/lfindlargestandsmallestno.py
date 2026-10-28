n = int(input("How many numbers? "))

if n <= 0:
    print("Enter a positive count")
else:
    num = int(input("Enter number 1: "))

    largest = num
    smallest = num

    for i in range(2, n + 1):
        num = int(input("Enter number: "))

        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

    print("Largest number =", largest)
    print("Smallest number =", smallest)