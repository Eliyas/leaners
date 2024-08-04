

## data type

##   list
##   Index   0      ,   1     ,    2    ,  3
myFruits = ["apple", 800, "banana", "cherry", "orange"]  # total fruits 4 (length of list)s

# syntax to access list
# listName[ index ]

print(myFruits[0])  
# apple

print(myFruits[3])
# orange



##  boolean
x = True

#display x:
print(x)

#display the data type of x:
print(type(x)) 


#  dict  dictionary
myDict = {
  "talk": "a person speaking",
  "modesty": "Indicates a quality"
}

myDictList = ["a person speaking", "Indicates a quality"]


myFruits = ["apple", "banana", "cherry", "orange", "strawberry"]

myFruitsColor = ["red", "yellow", "pin", "orange", "red"]

myFruitsColorsMap =	{
  "apple": "red",
  "banana": "yellow"
}


#  studentsIds 
studentIds = [90, 80, 78, 34]

#  studentsIdMap 
studentIds = {
  "basith": 90,
  "burhan": 80,
  "Apsar": 78,
  "buhari": 34
}

print(type(myDict))
print(myDict["talk"])
print(myDict["modesty"])

print(" Basith id is :" + str(studentIds["basith"]))
print(" Apsar id is :" + str(studentIds["Apsar"]))
print(" Apsar id is :" + str(studentIds.get("Apsar")))