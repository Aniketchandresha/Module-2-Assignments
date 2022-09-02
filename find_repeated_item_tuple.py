# Write a Python program to ﬁnd the repeated items of a tuple.

tup = ("apple","banana","cherry","kiwi","apple","kiwi")
# # print(tup)

# myset = set(tup)
# # print(myset)

# tupp = tuple(myset)
# print(tupp)

count = tup.count("apple")
count2 = tup.count("kiwi")
print(f"apple is repeat {count} times and kiwi is repeat {count2} times in the given tuple.")