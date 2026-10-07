try:
    num1 = int(input("Enter A First Number:"))
    num2 = int(input("Enter A Second Number:"))

    result = num1 / num2
    print("Result Is", result)

except ZeroDivisionError:
    print("Divison By Zero Is Error!!!!")

except ValueError:
    print("!Please Enter A Valid Whole Number!")

except:
    print("Wrong Input")

else:
    print("No Exceptions")

finally:
    print()