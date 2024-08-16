
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

# string formatting
a = " Hello, World! "
print(a)
print(a.upper())
print(a.lower())
print(a.strip())
print(len(a))
print(len(a.strip()))

#  Hello, World! 
#  HELLO, WORLD! 
#  hello, world! 
# Hello, World!
# 15
# 13

a ="Hello, World!"

replacedStr = a.replace("H", "J")
# replacedStr = "Hello, World!".replace("H", "J")
# "Jello, World!"
# replacedStr = "Jello, World!"

print(replacedStr)
print(a)
print(a.replace("W", "J"))
print(a)
# Jello, World!
# Hello, World!
# Hello, Jorld!
# Hello, World!