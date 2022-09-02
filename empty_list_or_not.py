# Write a Python program to check a list is empty or not. 

mylist = [] #created an empty list
n = int(input("Enter the number of elements : ")) #number of elements to be input
for i in range(0,n):
    element = input()
    mylist.append(element)
print(mylist)

list_length = len(mylist)
# print(list_length)

if list_length == 0:
    print("The list is empty")
else:
    print(f"The number of data you entered :{len(mylist)}")
