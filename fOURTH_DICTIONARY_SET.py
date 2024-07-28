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
Info["Address"] = "Amlapara,Narayangonj"
print("   ")
print(Info)