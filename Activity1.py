try:
    num = int(input("Enter A Number :  "))
    print("the Number Entered Is", num)
except ValueError as ex:
    print("Exception: ", ex)