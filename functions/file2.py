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


# Define a function named 'find_large_number_in_list' which takes one argument, 'given_list'
def find_large_number_in_list(given_list):
    max_num = 0
    for i in given_list:
        if i > max_num:
            max_num = i
 
    # Return the final value of 'max_num'
    return max_num
max_num = find_large_number_in_list([12,10,15,14])
print(max_num)

## Functio to count words in a sentence or string

def count_word_in_sentence(sentence):
    total_word = 0
    for words in sentence.split():
        total_word += 1
    return total_word

total_words = count_word_in_sentence("This is nice world!")
print(total_words)

## remove duplicate from the list

def remove_duplicate_from_list(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst

new_lst = remove_duplicate_from_list([1,2,1,4,5,2,10,11])
print(new_lst)

# alternate version of remove duplicate from the list

def remove_duplicate_from_list(lst):
    return list(set(lst))

new_lst = remove_duplicate_from_list([1,2,1,4,5,2,10,11])
print(new_lst)
