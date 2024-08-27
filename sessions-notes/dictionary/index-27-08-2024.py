myBrand =	{
  "brand": "Ford", 
  "model": "Mustang",
  "year": 1964
}

myBrand["color"] = "Blue"

# print(myBrand)

myBrand["model"] = "Land Rover"

# print(myBrand)

# print(myBrand.keys())
# print(myBrand.values())


myCar1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
myCar2 = myCar1.copy()
myCar2["model"] = "Range Rover"
myCar3 = myCar1.copy()
myCar3["model"] = "Punch"
print(myCar1)
print(myCar2)
print(myCar3)


