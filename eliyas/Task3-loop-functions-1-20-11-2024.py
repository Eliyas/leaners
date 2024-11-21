# 1. write a function to print odd numbers from the list.
# I/P: [4,2,5,1,6,8,12,9,3]
# O/P: 5, 1, 3, 9

# 2. write a function to print largest number from the list.
# I/P: [4,2,5,1,6,8,12,9,3]
# O/P: 12

# 2. write a function to print smallest number from the list.
# I/P: [4,2,5,1,6,8,12,9,3]
# O/P: 1

# 3. write a function to print odd characters from the given string.
# I/P: "myNameIsEliyas"
# O/P: m, N, m, I, E, i, a

# 4.  write a function to Reverse the given string
# I/P: "I Love You"
# O/P: "uoY evoL I"

## 5.  write a function to get number of vowels in the string
# I/P: "I Love You"
# O/P: 5


# a e i o u

# look strings one by one
# take one character and check the char is vowels
# if it is a vowel then store the count.
# I/P: "I Love You"
def getNumberOfVowels(inputString):
    countTemp = 0
    for i in inputString: 
        print(i)
        character = i.lower()
        if character == 'a': 
            countTemp += 1
        if character == 'e': 
            countTemp += 1
        if character == 'i': 
            countTemp += 1
        if character == 'o': 
            countTemp += 1
        if character == 'u': 
            countTemp += 1
    
    return countTemp

def getNumberOfVowels1(inputString):
    countTemp = 0
    for i in inputString: 
        print(i)
        if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u': 
            countTemp += 1

    return countTemp

def getNumberOfVowels2(inputString):
    countTemp = 0
    for i in inputString: 
        print(i)
        try: 
            if ['a', 'i', 'e', 'o', 'u'].index(i.lower()): 
                countTemp += 1
        except:
             print("Not a vowels")

    return countTemp

def getNumberOfVowels3(inputString):
    vowelsDict = { "a": True, 'i': True, 'e': True, 'o': True, 'u': True }
    countTemp = 0
    for i in inputString: 
            try: 
                if vowelsDict[i.lower()]: 
                    countTemp += 1
            except:
             print("Not a vowels")
             
    return countTemp

print("No of Vowels " + str(getNumberOfVowels("I Love You")))
print("No of Vowels " + str(getNumberOfVowels3("I Love You")))