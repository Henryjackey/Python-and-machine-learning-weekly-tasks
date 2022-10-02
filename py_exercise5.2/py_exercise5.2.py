largest = None
smallest = None

while True:
    num = input("Please enter a number: ")
    if num == "done":
        break

    try:
        num = int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
            smallest = num

    except ValueError:
        print("Input Error")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)