
# list creation
#  index           #   0     ,    1    ,   2     ,   3
myFruits1 =         ["apple", "banana", "cherry", "orange"]
# index from back  #   -4    ,  -3    ,  -2     ,   -1
myFruits2 = list(("apple", "banana", "grapes", "cherry", "orange"))

# -1 from last
print(myFruits1[-1])
# -2 from last
print(myFruits1[-2])

# -1 from front
print(myFruits1[0])
print(myFruits1[1])

# from middle with next 1 item
# arrayName[start:end] start => select where its starts ;  end => select before its ends
print(myFruits2[0:3])
print(myFruits2[:3])
print(myFruits2[:])


# from last
myFruits3 = list(("apple", "banana", "grapes", "cherry", "orange"))

# from last 
print(myFruits3[-4:-1])

# overriding item in the list
myFruits3[3] = "kiwi";
print(myFruits3)
