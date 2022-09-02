# Write a Python program to convert a list of characters into a string.

mylist=["1","Hello","Python",2,3,4]

x = ' '.join(str(i) for i in mylist)
print(x)