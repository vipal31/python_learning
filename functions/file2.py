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
    print(f"Your full name is {first_name} {last_name}")

print_full_name('Vipal','Gujrathi')

## function to print sum of list

number_list = [1,2,3,4,5]

def sum_of_list(input_list):
    list_sum = 0
    for i in number_list:
        list_sum += i
    
    return list_sum
sum_list = sum_of_list(number_list)
print(sum_list)

## find larget number for give list

def find_large_number