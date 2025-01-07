
# 1 
myCollegeName = "New College"
# Variable overrides
myCollegeName = "SRM"
print(myCollegeName)


# 2 print function

# comma separate print
x = "MY"
y = "Name is"
z = "Eliyas"
print(x,y,z)

# string concatinate print
x = "MY "
y = "Name is "
z = "Eliyas"
myName = x + y + z
print(myName)

myInt = 10 ## int(10)

# 3 carbage collection
x = "awesome"

def myFunc():
  yyy = "fantastic"
  print("1 yyy " + yyy)
  print("Python is " + x)

myFunc()

# yyy = "some value"
# cannot print since yyy is defined inside myfunc and it is carbage collected(variable destroyed)
#print("Python is  "+ yyy)

print("Python is " + x)