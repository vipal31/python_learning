#This is simple script to print if number if even or odd

try:
    num = int(input("Enter number: "))

    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
except ValueError:
    print("Please enter a valid number")

# This is a simple grade calculator script


try:
    num = int(input("Enter number: "))

    if num >= 90:
        print("Your grade is A")
    elif num >=80 and num <90:
        print("Your grade is B")
    elif num >=70 and num <80:
        print("Your grade is C")
    elif num >=60 and num <70:
        print("Your grade is D")
    else:
        print("Your grade is F")
except ValueError:
    print("Please enter a valid number")

## Sum of numbers, with input validation

try:
    num1 = int(input("Enter number: "))

    sum = 0
    for i in range(1, num1+1):
       sum += i
    print(sum)

except ValueError:
    print("Please enter a valid number")

# Multiplication table

try:
    num2 = int(input("Enter number: "))

    for i in range(1, 11):
        print(f"{num2} x {i} = {num2*i}")
except ValueError:
    print("Please enter a valid number")

