

apsarEducation = "Arts&Science"

if(apsarEducation == "Arts&Science"):
    print("Will become Software Eng")
elif apsarEducation == "Medical":
    print("Will become doctor")
elif apsarEducation == "Multimedia":
    print("Will enter into Cine field")
else:
    print("Will start a business")


a = 3300
b = 3300
# less than <
# greater than >
# equals ==
# not !=
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
elif b < a:
  print("b less than a")
else:
  print("a is greater than b")



apsarEducation = "Arts&Science"
interest = "Business"

if(apsarEducation == "Arts&Science"):
    if(interest == "Teaching"):
        print("Will become A Teacher")
    elif(interest == "Programming"):
       print("Will become Software Eng")
elif apsarEducation == "Medical":
    if(interest == "Teaching"):
        print("Will become medical college prof")
    else:
       print("Will start a clinic")
elif apsarEducation == "Multimedia":
    print("Will enter into Cine field")
else:
    print("Will start a business")


if(apsarEducation == "Arts&Science" and interest == "Teaching"):
    print("Will become A Programming Teacher")
elif apsarEducation == "Arts&Science" and interest == "Programming":
    print("Will become Software Eng")
elif apsarEducation == "MBA in business" or interest == "Business":
    print("Will start a business")

if apsarEducation == "Arts&Science" or interest == "Programming":
    print("Will become Software Eng")


if not apsarEducation == "Arts&Science": 
    print("Start a business");

if apsarEducation == "Arts&Science": 
    pass
else: 
    print("Start a business");
