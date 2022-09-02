'''Write a Python function that takes a list and returns a new list with unique
elements of the ﬁrst list.'''


# list1=[]
# n=int(input("How many elements do you want to add? "))
# for i in range(n):
#     ele = input()
#     list1.append(ele)
# print(list1)

list1=["Ram","Shyam","Ghanshyam","Nilkanth","Mahadev","Ramdev"]

list2=[]
for i in list1:
    if "dev" in i:
        list2.append(i)
print(list2)