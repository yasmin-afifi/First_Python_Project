def main():
    number = 0 
    while True:
        try:
            number = int(input('Enter a positive number: '))
            if number < 0:
                raise ValueError("please enter a positive number")
        except:
            print('please enter a positive number')
        else:
            break

    def factorial(number):
        if number == 0 or number == 1:
            return 1
        else:
            return number*factorial(number-1)

    factorial_result = factorial(number)
    return number,factorial_result


number,fact = main()
print(f"factorial of {number} = {fact}")