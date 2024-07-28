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


# Dictionary Methods 
# dict.keys()
print (NSU.keys()) #returns all the keys of the Dictionary

#Shifting the dictionary keys into a list . just typecast it
print(list(NSU.keys()))

# Number of total keys
print(len(NSU.keys()))
# OR
print(len(list(NSU.keys())))

# Dict.values returns all the values of the dictionary
print(NSU.values())
print(list(NSU.values()))
print(len(list(NSU.values()))) # returns the number of Keys not the number of values

# Dict.items returns the (key,values) pairs as tuples
print(NSU.items())
print(list(NSU.items()))
pairs = list(NSU.items())
print(pairs[0])
print(pairs[1])

# Dict.get("Key")
print(NSU["Marks1"])
print(NSU.get("Marks1")) #First these two return the same value 

#Second these two doesn't have the Key "Marks3" in the dict so ,
#print(NSU["Marks3"])   
# as a result NSU["Marks3"] will return error
print(NSU.get("Marks3"))
# but NSU.get("Marks3") it will return none value which won't create a hindrance running the program

# Dict.update
NSU.update({"Ph_Num1" : 1705395013,"City_01" : "Narayangonj"})
NSU["Ph_Num2"]=1838073738
NSU["City_02"]="Dhaka"
print(NSU,"\n")


# SETS 
set1 = {1,2,3,4,"Choco","Cake","Chips"}
print(set1)
print(len(set1))
# (repeated values are not allowed in sets)
# it will return just 2,3,choco,cake
set2 = {2,2,3,3,"Choco","Cake","Choco"} 
print(set2)
print(len(set2))

# empty set
collect = set()
print(collect)
collect.add("Numbers")
collect.add(12)
collect.add(23)
collect.add(35)
collect.add("Tuples")
collect.add((48,63))
print(collect)
collect.remove("Tuples")
collect.remove(23)
print(collect)
# we can not insert list in a set
print(collect.pop())
print(collect)
collect.clear()
print(collect)

#Union and Intersection

s1 = {1,2,3}
s2 = {3,4,5,6}
s3 = s1.union(s2)
print(s3)
s4=s1.intersection(s2)
print(s4)

# 1st Program

# Marks = {}

# num = int(input("Enter phyics marks : "))
# Marks.update({"Physics" : num})
# num = int(input("Enter Chemistry marks : "))
# Marks.update({"Chemistry" : num})
# num = int(input("Enter Math marks : "))
# Marks.update({"Math" : num})
# print(Marks)

