# Write a Python program to replace last value of tuples in a list. 

tup = ("apple","banana","cherry","kiwi")
mylist = list(tup)
mylist[-1]="pineapple"

tupp = tuple(mylist)
print(tupp)