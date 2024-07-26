
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

# 3 carbage collection
x = "awesome"

def myfunc():
  yyy = "fantastic"
  print("1 yyy " + yyy)
  print("Python is " + x)

myfunc()

# yyy = "some value"
# cannot print since yyy is defined inside myfunc and it is carbage collected(variable destroyed)
#print("Python is  "+ yyy)

print("Python is " + x)