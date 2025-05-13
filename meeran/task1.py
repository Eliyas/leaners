# add item into the list
myList = ["apple", "banana", "cherry"]
myList.insert(1,"berry")
print(myList) 


# Remove an item from the list  
mylist2 = ["apple", "banana", "cherry", "banana", "kiwi"]
# Remove cherry from the list  
mylist2.remove("banana")
print(mylist2)


#copy few items from a list to another list
mylist3 =["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist3[4:6])


#copy few items from a list to another list
mylist4 =["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist4[4:7])


#replace "banana" to "berry"
myList5 = ["apple", "banana", "cherry"]
myList5[1:3] = ["berry","orange"]
print(myList5)


#replace "cherry" to "orange"
myList6 = ["apple", "banana", "cherry"]
myList6[2]= "orange"
print(myList6)
