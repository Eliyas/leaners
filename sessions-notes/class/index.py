class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    ## self => p1 instance (context of the p1)
    def displayName(self, prefix):
        return prefix + " " + self.name
  	
    def setName(self, name):
  	    self.name = name

p1 = Person("John", 36)



print(p1.name)
p1.setName("Meeran")
print(p1.name)
print(p1.displayName("Mr"))
