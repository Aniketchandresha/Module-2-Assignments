# Write a Python program to remove an empty tuple(s) from a list of tuples.

tuplex = ("apple","banana","cherry","orange","mango")
tupley = ()
# print(tuplex)
# print(tupley)

if len(tuplex) == 0 :
    del tuplex
else:
    print(tuplex)

if len(tupley) == 0:
    del tupley
else:
    print(tupley)