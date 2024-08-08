myFruits = ["apple", "banana", "cherry"]
myFruits1 = myFruits.copy()
myFruits1.append("berry")
myFruits.append("orange")
# print(myFruits)
# print(myFruits1)


# copy without reference 
basithBasket = ["apple", "banana", "cherry"]
meeranBasket = basithBasket.copy()

basithBasket.append("Tea Powder")
meeranBasket.append("washing powder")

print(basithBasket)
print(meeranBasket)

# 3 way of copy without reference
basket = ["apple", "banana", "cherry"] # 1
basket1 = list(basket) # 2
basket2 = basket[:] # 3