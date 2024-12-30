while True:
    try:
        first_number = int(input('Enter the first number= '))
        second_number = int(input('Enter the second number= '))

        sum = second_number+first_number
        subtraction = first_number-second_number
        multiplication = second_number*first_number
        division = first_number/second_number
    except ZeroDivisionError:
        print("You can not divide by zero,try again")
    else:
        print("--------------------------")
        break

print(f"sum={sum}")
print(f"subtraction={subtraction}")
print(f"multiplication={multiplication}")
print(f"division={division}")
