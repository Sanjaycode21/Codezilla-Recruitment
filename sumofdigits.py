y = "y"
while y == "y":
    a = input("Enter a number: ")
    s = 0
    if a.isnumeric():
        for i in a:
            s += int(i)
        print("Sum of the entered digits is:", s)
        y = input("Do you want to continue? <y/n>: ")
        if y.lower() != "y":
            break
    else:
        print("Invalid Input! Enter a valid number!")