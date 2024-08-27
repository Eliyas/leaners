mydict =	{
  "brand": "Ford", 
  "model": "Mustang",
  "year": 1964
}


myList = []
myTuple = ()
mySet = {}
myDict = {"brand": "Ford"}
# property "brand": "Ford" 
# key "brand" 
# value "Ford"

print(mydict)
print(mydict.get("brand"))
print(mydict["brand"])

myBankVault = {
    "key1": ["jewels", "money", "diamond"],
    "key2": ["jewels", "money", "diamond"],
}

myList = [
    "1",
    24,
    254,
    3535
]

print(myBankVault["key1"])
print(myBankVault["key1"][0])

# myList = ["jewels", "money", "diamond"]
# print(myList[0])

myList = ["Ford", "Mustang", 1964, "Tata", "Safari", 1954]

myList = [
{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
},
{
  "brand": "Tata",
  "model": "Safari",
  "year": 1954
}
]


myBankVault = {
    "key1": ["jewels", "money", "diamond"],
    "key2": ["jewels", "money", "diamond"],
}

print(myBankVault["key1"][0])
print(myBankVault["key1"][1])
print(myBankVault["key1"][2])

myBankVault = {
    "eliyasLocker": { 
        "money": 8436868168, "jewels": "6772kg", 
        "subLocker1": {
                "dimond": "91879kg",
                "subLockersDuplicateKey": ["key1", "key2"]
                } 
        },
    "basithLocker": { "money": 52552352, "jewels": "5645kg", "dimond": "4764kg"}
}

print(myBankVault["eliyasLocker"]["subLocker1"]["subLockersDuplicateKey"][0])




print("Eliyas's Diamond " + myBankVault["eliyasLocker"]["subLocker1"]["dimond"])
print(myBankVault["eliyasLocker"])
print(myBankVault["basithLocker"])
print("Eliyas's Money "+ str(myBankVault["eliyasLocker"]["money"]))
print("Basith's Money "+ str(myBankVault["basithLocker"]["money"]))
print("Basith's Jewel "+ str(myBankVault["basithLocker"]["jewels"]))
