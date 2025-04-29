# Basic variable examples, it will print my name, age and height on the screen
name = 'Vipal'
age = 38
height = 1.55

print("Hello all, my name is {} and I am {} years old with {} m height".format(name,age,height))
## This script ask user for their age, convert to int and print type of age variable

user_age = input("Please enter your age: ")
user_age = int(user_age)

print(type(user_age))

# This command will convert one variable to int and add to other variable

num_str = "3.14"
num_int = 5

num_str = float(num_str)

total = num_str + num_int
print(total)