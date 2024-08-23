


#  car is object
#  engine, tyre, steering, gear, break  are properties
#  running, forward, reverse, break, driving are action


def drive(): 
    print("driving")

def breaking():
    print("driving")

myCarDict = {
    "prop1": "engine",
    "prop2": "tyre",
    "prop3": "steering",
    "drive": drive,
    "break": breaking
} 


# creating objects for every employee from class
class Employee:
    # object constructor
    def __init__(basithEmp, firstName, lastName, age):  #  arguments
        basithEmp.firstName = firstName
        basithEmp.lastName = lastName # private variables
        basithEmp.age = age

    # class methods or functions
    def getEmployeeFirstName(self):
        return self.firstName

    def getEmployeeAge(self):
        return self.age
    
    def getEmployeeName(self):
        return self.firstName + " " + self.lastName
    


# object is an instance of an class
basithEmp = Employee("Mohmed", "Basith", 50);  # parameters
apsarEmp = Employee("Mohmed", "Apsar", 60);

print(basithEmp.getEmployeeName())
print(basithEmp.getEmployeeAge())

print(apsarEmp.getEmployeeName())
print(apsarEmp.getEmployeeAge())


#  creating separate dict for every employee
def getEmployeeName(self):
    return self['name']

def getEmployeeAge(self):
    return self['age']
    

basithEmpDict = {
    "name": "Basith",
    "age": 50,
    "getEmployeeName": getEmployeeName,
    "getEmployeeAge": getEmployeeAge
} 

#  square []    circle ()
# print(basithEmpDict["getEmployeeName"](basithEmpDict))
# print(basithEmpDict["getEmployeeAge"](basithEmpDict))


apsarEmpDict = {
    "name": "Apsar",
    "age": 60,
    "getEmployeeName": getEmployeeName,
    "getEmployeeAge": getEmployeeAge
} 

# print(apsarEmpDict["getEmployeeName"](apsarEmpDict))
# print(apsarEmpDict["getEmployeeAge"](apsarEmpDict))
