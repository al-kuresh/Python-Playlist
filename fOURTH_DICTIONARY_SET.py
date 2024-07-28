# dictionary's key can't be changed but the values can be changed
Info = {
     # KEY = Value
     "Name"       : "Al Kuresh Muna",
     "Age"        : 18,
     "Profession" : "Student",
     "is_Adult"   : True,
     "Cgpa"       : 3.79,
     "Subjects"   : ["Cse","ECE"],
     "Batch"      : ("Batch: ",222)

}
print(Info)
print(Info["Name"])     #we can print dictionary values separately by Info["Key"] = value
print(Info["Subjects"])

Info["Name"] = "Faisal"
Info["Address"] = "Amlapara,Narayangonj"  # We can add a new Key in the Dictionary by assigning this way
print("   ")
print(Info)

# Nested Dictionary

NSU = {
    "Student1" : "Saif",
    "Marks1" : {
        "phy"   : 98,
        "che"   : 95,
        "Math"  : 90
    },
    "Student2" : "Ratan",
    "Marks2" : {
        "Phy" : 84,
        "Che" : 76,
        "Math": 100
    },
}

print(NSU)
print("  ")
print(NSU["Marks1"]["Math"])