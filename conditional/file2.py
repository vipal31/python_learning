#sum of all numberss from 1 to a give number
enter_number = int(input("Enter a number: "))
sum_of_numbers = 0
for i in range(1, enter_number + 1):
    sum_of_numbers += i
print(sum_of_numbers)

# Print multiplication table of a given numbe

num = 2
for i in range(1, 11):
    #print(num, "x", i, "=", num * i)
    print(num * i)

#display numbers from list using loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)