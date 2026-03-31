# list are ordered collection of data items
# store multiple items under single variable

Name=["raj", "Kapoor","Laddu","Chunnu"]

print(Name[0])
print(Name[1])
print(Name[2])
print(Name[3])
print(Name[-3])


if "Kapoor" in Name:
    print("Yees,she is")

    print(Name)
    # print(Name[2:])
    # print(Name[:3:1])
    # print(Name[0:3:1])

Name.pop()
Name.append("Whom")
Name.remove("Laddu")
Name.insert(0,"Whom")
Name.reverse()
Name.sort()

# print(dir(Name))
# print(len(Name))
 



 
    # List=[] ordered and changable, Duplicates OK
    # Set={} unordered and immutable, add/remove ok 
    # Tuple() ordered and unchangable. Duplicates OK . Faster

Fruit=["apple","Banana"]

Fruit.append("orange")
Fruit.insert(1,"orange")
Fruit.insert(2,"0601")
print(Fruit)

Fruit.reverse()


tup=(1,2,3,)

print(tup[1])
print(tup[2])
# print(tup[3])  0ut of range 

if 7 in tup:
    print("ya its exist")
else:
    print("no its doesn't")
