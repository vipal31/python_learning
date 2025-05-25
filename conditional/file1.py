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
    elif num >=80:
        print("Your grade is B")
    elif num >=70:
        print("Your grade is C")
    elif num >=60:
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

### Guess the random number

import random

random_number= random.randint(1,20)
print("You need to guess a number between 1 to 20, you will have 3 attempts")
attempt = 3
while attempt >0:

    try:
       user_number = int(input("Enter a number to guess: "))
       ## decrase the attempt
       attempt -= 1
       if user_number == random_number:
           play_again = input("Bingo, correct number, Play again? (y/n): ")
           # Ask for User want to play again
           if play_again == 'y':
               random_number = random.randint(1,20)
               print("New Game started")
               attempt = 3
           else:
               print("Thanks for playing, Good Bye")
               break
           
       
       # if wrong guess, check the attempt
       elif attempt == 0:
           print(f"You loose! The correct number {random_number}. Thanks for playing!")
           play_again = input("Would you like to play again? (y/n): ")
           if play_again == 'y':
                random_number = random.randint(1,20)
                attempt = 3
                print("New Game Started")
           else:
                print("Thanks for playing")
                break

       else:
           # Only print message if attempt remain
           
           if user_number > random_number:
                print("To high, try again")
                print(f"You have {attempt} remaining")
           else:
               print("To low, try again")
               print(f"You have {attempt} remaining")
            
    except ValueError:
        print("Please enter a valid number")
        attempt -= 1

### pizza ordering
print("Welcome to the Python pizza delivery!")
size = input("Please enter the size of pizza you wish to order? S.M Or L: ").lower()
pepperoni = input("Do you wish to add pepperoni in your pizza? Y or N: ").lower()
extra_cheese= input("Do you wish to add extra_cheese on your pizza? Y or N: ").lower()

final_bill = 0

if size == "l":
    ## large size pizz will be $25
    pizza_cost = 25
    if pepperoni == 'y':
        ## Peperoni will be $3 extra
        pepperoni_cost = 3
        if extra_cheese == 'y':
            ## extra cheese will cost $1 extra
            cheese_cost = 1
            final_bill = pepperoni_cost + cheese_cost + pizza_cost
            print(f"Your total bill will be ${final_bill}")
        else:
            final_bill = pepperoni_cost + pizza_cost
            print(f"Your final bill would be {final_bill}")
    elif pepperoni == 'n':
        if extra_cheese == 'y':
            ## extra cheese will cost $1 extra
            cheese_cost = 1
            final_bill = cheese_cost + pizza_cost
            print(f"Your total bill will be ${final_bill}")     
        else:
            final_bill = pizza_cost
            print(f"Your total bill will for large size pizza ${final_bill}")

elif size == 'm':
    # medium pizza cost $20
    medium_pizza_cost = 20
    if pepperoni == 'y':
        ## Peperoni will be $3 extra
        pepperoni_cost = 3
        if extra_cheese == 'y':
        ## extra cheese will cost $1 extra
            cheese_cost = 1
            final_bill = medium_pizza_cost + pepperoni_cost + cheese_cost
            print(f"Your total bill will be ${final_bill}")
        else:
            final_bill = medium_pizza_cost + pepperoni_cost
            print(f"Your total bill will be ${final_bill}")
    elif pepperoni == 'n':
        if extra_cheese == 'y':
            ## extra cheese will cost $1 extra
            cheese_cost = 1
            final_bill = medium_pizza_cost + cheese_cost
            print(f"Your total bill will be ${final_bill}")
        else:
            final_bill = medium_pizza_cost
            print(f"Your total bill will be ${final_bill}")

else:
    #small size pizza cost
    small_pizza_cost = 15
    if pepperoni == 'y':
        ## Peperoni will be $2 extra
        pepperoni_cost = 2
        if extra_cheese == 'y':
            ## extra cheese will cost $1 extra
            cheese_cost = 1
            final_bill = small_pizza_cost + pepperoni_cost + cheese_cost
            print(f"Your total bill will be ${final_bill}")
        else:
            final_bill = small_pizza_cost + pepperoni_cost
            print(f"Your total bill will be ${final_bill}")
    elif pepperoni == 'n':
        if extra_cheese == 'y':
            ## extra cheese will cost $1 extra
            cheese_cost = 1
            final_bill = small_pizza_cost + cheese_cost
            print(f"Your total bill will be ${final_bill}")
    else:
        final_bill = small_pizza_cost
        print(f"Your total bill will be ${final_bill}")
    

# second attempt

bill = 0

if size == 's':
    bill += small_pizza_cost
elif size == 'm':
    bill += medium_pizza_cost
else:
    bill += pizza_cost

'''
pepperoni
'''
if pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

"""extra_cheese"""

if extra_cheese =='y':
    bill += 1