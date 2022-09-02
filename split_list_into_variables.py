# Write a Python program to split a list into diﬀerent variables. 

a = [1,2,3,4,5,6,7,8,9]
b = a[:len(a)//2]
c = a[len(a)//2:]

d = ''.join(str(i) for i in b)
e = ','.join(str(i) for i in c)

print(d)
print(e)
