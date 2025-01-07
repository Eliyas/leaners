
#sort

thislist1 = ["orange", "mango", "kiwi", "apple", "pineapple", "banana"]

thislist1.sort()

thislist2 = [3,5,8,9,1]
thislist2.sort()

print(thislist2)
# print(thislist2)

# sorting with caps letters
thislist3 = ["orange", "mango", "kiwi", "pineapple", "candy", "apple", "banana", "zeebra", "Apple", "Candy", "Banana"]

thislist3.sort()

print(thislist3)
# O/P ['Apple', 'Banana', 'Candy', 'banana', 'candy', 'kiwi', 'mango', 'orange', 'pineapple', 'zeebra']

# descending order
thislist4 = ["orange", "mango", "kiwi", "pineapple", "candy", "banana", "zeebra", "Apple", "Candy", "Banana"]

thislist4.sort(reverse = True)

# print(thislist4)
# ['zeebra', 'pineapple', 'orange', 'mango', 'kiwi', 'candy', 'banana', 'Candy', 'Banana', 'Apple']


# reverse moves last items to first
thislist5 = ["orange", "mango", "kiwi", "apple", "pineapple", "banana"]

thislist5.reverse()

# print(thislist5)


# reference copy in list
myFruits = ["apple", "banana", "cherry"]
myFruits1 = myFruits
myFruits1.append("berry")
#myFruits.append("mango")
# print(myFruits1)
# print(myFruits)


# reference in literals
myFruit = "apple"
myFruit1 = myFruit
myFruit1 = "banana"
# print(myFruit1)
# print(myFruit)

myVar = "apple"
myVar1 = myVar
myVar = "banana"
# print(myVar1)
# print(myVar)


myFruits = ["apple", "banana", "cherry"]
myFruits1 = myFruits
myFruits2 = myFruits
myFruits1.append("berry")
myFruits2.append("Orange")
print(myFruits)
print(myFruits1)
print(myFruits2)


