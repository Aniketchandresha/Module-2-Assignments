# Write a Python program to remove duplicates from a list. 

list1=[1,2,3,4,5,1,2,3,4,5,"a","b","c","a","b","c"]
print(list1)

list2= list(dict.fromkeys(list1)) #here we convert list to dictonary and again to list
print(list2)

list3 = [*set(list1)] # here we use set to change a list to set which does not allow duplicates
print(list3)
