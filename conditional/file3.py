marks = [12,40,35,86,75,13,18,66,90,95,87]

min_number = 0

for mark in marks:
    if mark < min_number or min_number == 0:
        min_number = mark
print(f"The minimum number in the list is: {min_number}")


## add 1- 100

sum_of_100_numbers = 0
for i in range(1, 101):
    sum_of_100_numbers += i

print(f"The sum of numbers from 1 to 100 is: {sum_of_100_numbers}")