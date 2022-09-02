'''Write a Python function to get the largest number, smallest num and sum
of all from a list. '''

from tkinter import N


numbers = [5,10,15,20,25,30]

# print(f" The maximum number is : {max(numbers)}")
# print(f" The maximum number is : {min(numbers)}")
# print(sum(numbers))

highest = 0
for n in numbers:
    if n > highest:
        highest = n
print(f" The maximum number is : {highest}")

# lowest = 0
# for number in numbers:
#     if number < lowest:
#         lowest = number
# print(f" The minimum number is : {lowest}")

total = 0
for i in numbers:
    total += i
print(f" The sum is : {total}")



