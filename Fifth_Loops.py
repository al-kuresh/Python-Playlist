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
# MULTIPLICATION OF ANY NUMBER
num  = int (input("Enter numberL: "))
i = 1
while i<=10:
    print(num*i)
    i+=1
print("   ")
# Print the values of the list
list = [1,4,9,16,25,36,49,64,81,100]
length1 = len(list)
i=0
while i<=(length1-1):
    print(list[i])
    i+=1
print("   ")
# Search for a number in Tuple
tup = (1,4,9,16,25,36,49,64,81,100)
x  = int (input("Enter numberL: "))
length2 = len(tup)
i=0
while i<=(length2-1):
    if(x==tup[i]):
        print(x,"number is found in tuple")     
    i+=1 