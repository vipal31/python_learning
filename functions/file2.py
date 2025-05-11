#basic function

def print_message():
    print("This is my first function")

print_message()

# function to calculate are of square

def area_of_rectangle(length, width):
    area = length * width
    return area

areas = area_of_rectangle(4,4)
print(f"Area of a given rectangle is {areas}")

## function to print if number is even or odd

def is_even(number):
    return number % 2 == 0
        
result = is_even(4)
print(f"The number 4 is {
    'even' if result else 'odd'}"
)

# print full  name,last name

def print_full_name(first_name, last_name):
    print("Your full name is {} {}".format(first_name ,last_name))

print_full_name('Vipal','Gujrathi')