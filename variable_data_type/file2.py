## This small script will do simple interest calculation

principal_amount = int(input("Please enter total principal amount: "))
rate_of_interest = float(input("Please enter your ROI: "))
loan_tenure = int(input("Please enter your loan tenure: "))

Simple_interest = (principal_amount * rate_of_interest * loan_tenure) / 100

print("Total interest amount for loan would be {}".format(Simple_interest))


## This small script will calculate area of a circle

from itertools import count
import math
radius_of_circle = int(input("Enter radius of a circle in m: "))
area_of_circle = math.pi * radius_of_circle**2
print("Area of circle is {:.3f}".format(area_of_circle))

## This small script is to learn string manipulation, it will convert sentence to lowercase, count the words in it

user_sentence = input("Enter your favorite sentence: ")
user_sentence_lowercase = user_sentence.lower()
print(len(user_sentence_lowercase.split()))
print(user_sentence_lowercase)

## This will be an example of boolean logic, ask user if he/she is student, have job and eligible of loan

student_name = input("Enter your name: ")
input1 = input(f"{student_name}, are you a student?,Enter Yes or No:" ).lower()
input2 = input(f"{student_name} do you have a job?, Enter Yes or No:").lower()

if input1 == "yes" and input2 == "no":
    print(f"{student_name}, You are eligible for loan!")
else:
    print(f"Apologize, {student_name} you are not eligible for loan")

## Small example of currency conversion

usd_amount = int(input("Enter amount in USD: "))
indian_rupee = usd_amount * 85
print(f"You will have INR {indian_rupee=:.3f}")

## Combine data type

book_detail = {}
book_detail.update({"title" : "Atomic Habits", "Author" : "James Clear", "price" : 9.10, "in_stock" : True})

for key, value in book_detail.items():
    print(key, value)