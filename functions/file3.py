#function to chek if vowel exist in string

def count_vowel(text):
    sum_vowel = 0
    vowels = 'aeiou'
    for char in text.lower():
        if char in vowels:
            sum_vowel +=1
    return sum_vowel

vowel = count_vowel("America")
print(vowel)

## Another version of this function

def count_vowels(text):
    vowels = 'aeiouAEIOU'  # Include both upper and lower case
    sum_vowels = 0
    vowels_found = []  # To keep track of which vowels were found

    for char in text:
        if char in vowels:
            sum_vowels += 1
            vowels_found.append(char)

    # Provide detailed output
    if sum_vowels > 0:
        print(f"Found {sum_vowels} vowels: {', '.join(vowels_found)} in {text}")
    else:
        print(f"No vowels found in '{text}'")

    return sum_vowels

# Test the function
print(count_vowels("America"))  # Should show which vowels were found
print(count_vowels("Sky"))      # Should indicate no vowels found


## function to reverse the string

def reverse_string(text):
    return text[::-1]

result1 = reverse_string('Vipal')
print(result1)

## find common element in two list 

def common_element_in_list(list1,list2):
    common = []
    for i in list1:
        if i in list2:
            common.append(i)
    return common

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8,10,12,14,16,18,20]

result = common_element_in_list(list1,list2)
print(result)