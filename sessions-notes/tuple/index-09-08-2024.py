


thistuple = ("apple", "banana", "cherry")
#thistuple[0] = "berry" # unchangeable
print(thistuple)



y = 50
y = y + 10
# short for of add and assign like above
y += 10


# unpacking
fruits = ("apple", "banana", "cherry", "orange", "berry")

(a, b, *c) = fruits
(d,e,f) = c

print(a)
print(b)
print(c)

print(d)
print(e)
print(f)



# tuple update
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# tuple union
set11 = {"a", "b", "c"}
set12 = {1, 2, 3}

print(set11)
print(set11.union(set12))


# difference
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple", "FB", "cherry"}

set3 = set1.difference(set2)
set4 = set2.difference(set1)
print(set3)
print(set4)