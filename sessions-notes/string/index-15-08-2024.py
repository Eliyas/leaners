# to check character pattern in the string
txt = "The best things in life are free!"

print("s in l" in txt)
# true

txt = "The best things in life are free!"

print("things in" in txt)
# true

txt = "The best things in life are free!"

print("free! " in txt)
# false

#slice
b = "Hello, World!"
print(b[7:13])
print(b[7:12])
print(b[7:14])
print(b[0:5])
print(b[0:6])
print(b[0:8])

#print
# World!
# World
# World!
# Hello
# Hello,
# Hello, W

# slice
b = "Hello, World!"
print(b[:])
# Hello, World!
