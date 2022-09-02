# Diﬀerentiate between append () and extend () methods? 

actors = ["Ajay","Akshay","John","Hritik","Amitabh"]

#append is used to add some specific item in the list
actors.append("Shahrukh")
print(actors)

actresses = ["kareena","Katrina","Priyanka","Esha"]

#extend is used to merge two or more list items together
actors.extend(actresses)
print(actors)