fruits = ["apple", "banana", "cherry", "apple", "apple", "berry"]
# loops: 1 "apple", 2 "banana", 3 "cherry", 4 "apple"
#for fruit in fruits:
  #print(fruit)
 # print("Printed 1 fruit")

leaners = ["Basith", "Meeran", "Apsar", "Eliyas"]
# loops: 1 "apple", 2 "banana", 3 "cherry", 4 "apple"
for leaner in leaners:
  print("Mr."+ leaner + " is a Leaner \n")

fruits = ["apple", "banana", "cherry", "berry", "apple", "banana"]

# print only first found apple
for fruit in fruits:
  if(fruit == "berry"):
    print(fruit)
    break

aboutApsar = "Apsar is a business man"
condition = "fisherman" in aboutApsar

myChar = "nana"

## print the first fruit with character "nana"
for fruit in fruits:
  if(myChar in fruit):
    print(fruit)
    break

for char in "sport":
  print(char)



fruits = ["apple", "banana", "cherry", "berry", "apple", "banana"]

# print all fruits except apples
# 1
for fruit in fruits:
  if(fruit != "apple"):
    print(fruit)

# 2
for fruit in fruits:
  if(fruit == "apple"):
    continue

  print(fruit)