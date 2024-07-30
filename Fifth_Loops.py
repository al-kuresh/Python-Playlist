# WHILE LOOP 
# WHILE CONDITION:
        # STATEMENT
        # INCREMENT
i = 1
while  i<=5: 
    print("Good Morning")
    i+=1
# PRINTING 1 TO 5
i = 1
while  i<=5: 
    print(i)
    i+=1
print("   ")

#PRINTING 100 TO 1
i =100
while i>=1:
    print(i)
    i-=1
print("   ")
# # MULTIPLICATION OF ANY NUMBER
# num  = int (input("Enter number to multiply: "))
# i = 1
# while i<=10:
#     print(num*i)
#     i+=1
# print("   ")


# # Print the values of the list
# list = [1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<=(len(list)-1):
#     print(list[i])
#     i+=1
# print("   ")


# # Search for a number in Tuple
# tup = (1,4,9,16,25,36,49,64,81,100)
# x  = int (input("Enter number to search: "))
# length2 = len(tup)
# count = 0
# i=0
# while i<=(length2-1):
#     if(x==tup[i]):
#         count =1
#     i+=1


# if(count==1):
#     print(x,"number is found") 
# elif(count==0):
#     print(x,"number is not found")   


#Continue 

i = 1
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1

#For Loops
# For (any variable name) in (any list name)

list = ["Kuresh","MUna","Niloy"]
for val in list:
    print(val)
print("   ")

list1 = [1,2,3,4,5]
for val1 in list1:
    print(val1)
print("   ")

tup = ("Hridoy","Faisal","Nixon")
for val2 in tup:
    print(val2)
print("   ")

str = "North South Univarsity"
for char in str:
    print(char)

# Searching a number in tupple
various = []
size = int (input("Enter the size of the List: "))
i=1
while i<=size:
    x = int (input("enter number: "))
    various.append(x)
    i+=1

tp = tuple(various)
print("Printing the tuppple without for loop:-",tp)
x= int (input("Searching number: "))
count=0

for val in tp:
    if(val == x):
        count=1

if(count==1):
    print(x,"number is found")
else:
    print(x,"number is not found")    