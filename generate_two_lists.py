'''Write a Python function that takes two lists and returns true if they have
at least one common member. '''

#creating input list1 
mylist =[]
n = int(input("How many elements do you want to add? "))
for i in range(0,n):
    element = input()
    mylist.append(element)
# print(mylist)

#creating input list2
mylist2 =[]
n1=int(input("How many elemnts do you want to add in list 2? "))
for i in range(0,n1):
    ele = input()
    mylist2.append(ele)
# print(mylist2)

# list1=[1,2,3,4,5,6,7,8,9,0]
# list2=[2,3,4]

# x=set(list1)
# y=set(list2)

#changing list to a set to fix the items of the list
x=set(mylist)
y=set(mylist2)

z=x.intersection(y)
a = list(z)

if len(a) >= 1:
    print("true")
else:
    pass