valid = False

while not valid:
    try:
        num = int(input("Enter a Number: "))
        while num % 2 == 0:
            print("Bye")
            num = int(input("Enter a Number: "))
        valid = True

    except ValueError:
        print("Invalid!")