

myList = [2,4,5,6,7,8,9]
print(2 in myList)


# overried multiple items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

#thislist[1:3] = ["blackcurrant", "watermelon"]

thislist[3:5] = ["blackcurrant", "watermelon"]

print("this List")
print(thislist)

# without one value
thislist2 = ["apple", "banana", "cherry", "orange", "jack fruit"]

thislist2[2:] = ["blackcurrant", "watermelon"]

print(thislist2)

# insert without replace

""" class list:
    def insert(startIndex, item):
        return 0; """

        
thislist3 = ["apple", "banana", "cherry"]

thislist3.insert(1, "watermelon")

print("List 3") 
print(thislist3) 



thislist4 = ["apple", "banana", "cherry"]
thislist4.append("orange")
print(thislist4)


thislist5 = ["apple", "banana", "cherry"]

thislist5.append("dragon")
thislist5.append("berry")

print(thislist5)

#  extend

myFruits = ["apple", "banana", "cherry"]
myFruits2 = ["kiwi", "orange", "berry"]

myFruits.extend(myFruits2)

print(myFruits) 

# removes first item that matches
thislist = ["banana", "apple", "cherry"]
thislist.remove("banana")
print(thislist)


