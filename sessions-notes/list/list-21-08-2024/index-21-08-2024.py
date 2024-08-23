# List is a collection which is 1, ordered and 2, changeable. 3, Allows duplicate members.
# Tuple is a collection which is 1, ordered and 2, unchangeable. 3, Allows duplicate members.
# Set is a collection which is 1, unordered, 2, unchangeable*, and 3, unindexed. No duplicate members.

thislist1 = ["apple", "banana", "cherry", "berry", "orange"]
print(thislist1)
print(thislist1[1]) # banana
print(thislist1[-4]) # banana

thislist2 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist2)

# item override
thislist3 = ["apple", "banana", "cherry", "berry", "orange"]
thislist3[2] = "papaya"

thislist4 = ["apple", "banana", "cherry", "berry", "orange"]
print(thislist4[1])


list5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list5[:])
# list5[:] same like this list5[0:7]

list6 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list6[1:3] = ["blackcurrant", "watermelon", "papaya"]
print(list6)

# important methods
# insert, append, pop, sort, remove, extend

list7 = ["apple", "banana", "cherry"]

list7.append("orange")
list7.append("papaya")
list7.append("melon")

print(list7)


list8 = ["apple", "banana", "cherry", "orange", "papaya", "melon"]

print(list8.pop())
print(list8.pop())
print(list8.pop())
# melon
# papaya
# orange

thislist = ["apple", "banana", "cherry"]
# thislist.remove("bananA")
# ValueError: list.remove(x): x not in list
print(thislist)


list9 = ["banana", "apple", "Orange", "Kiwi", "cherry", "Apple"]
list9.sort()
print(list9)
list9.sort(key = str.lower)
print(list9)

list10 = ["Balaji", "burhan", "Alpha", "aravind", "anand", "Gopi", "gopal"]
list10.sort()
print(list10)
list10.sort(key = str.lower)
print(list10)



thisset1 = {"apple", "banana", "cherry"}
thisset1.remove("banana")
print(thisset1)

thisset2 = {"apple", "banana", "cherry"}
thisset2.discard("bananA")
print(thisset2)