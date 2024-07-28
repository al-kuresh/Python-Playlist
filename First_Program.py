print("Kuresh")
print("My age is 23")
#same line using coma , coma won't visible in the Output
print("Varsity Student","NSU")
#Printing Numbers 
print(45)  
#Operations in Numbers                    
print(45+15, 45-15 , 5*4 , 20/10)

#initializing Variable String Number 
Name = "Shiwli"
Age = 49
Relation = "Mother"
print(Name,Age,Relation)
print("         ")
Age = 53
Marks = 47.2594
# Printing values with sentences
print("Mother's name: ",Name)
print("Age is: ",Age)
print("Realtion with Kuresh: ",Relation)

#Printing the Data Types
print(type(Name))
print(type(Age))
print(type(Relation))
print(type(Marks))

#MULTI LINE COMMENT
"""
Adding
up
"""
# Ctrl + / for multiple hastags
a=10
b=5
sum = a+b
print("Sum = ",sum)

c=7
d=3
print(c%d)

num1=4
num2=3
print(num1,"^",num2,"=",num1 ** num2) # ** is for power (4^3) num1^num2

#relational operator
num=10
num+=5
print(num)

#Logical Operator AND OR NOT
print(not False) #True
print(not True) #False
print("         ")

Val1 = True
Val2 = False
print("Printing AND operator = ", Val1 and Val2) #False
print("Printing AND operator = ", Val1 or Val2) #True

#TypeCasting
word = "2"
number = 5
print(int(word) + number) #string to integer
print("         ")
#input String 
"""
 Name= input("Enter My name: ") #input entered in python as string
 print("User entered = ",Name)
"""
 
"""
Val1=input("val1 = ")
Val2=input("val2 = ")
sum=int(Val1)+int(Val2) #type casting the value to integer from str
print(sum)

"""

#typecasting the input() function 
# Val1= int (input("val1 = "))
# Val2= int (input("val2 = "))
# sum=Val1+Val2 
# print(sum)

# # MULTIPLICATION OF TWO NUMBERS USING INPUT
# var = float(input("Enter a float Number: "))
# var1 = float ( input("Enter a float number: "))
# multi = var*var1
# print("The Multiplication: ",multi)

# AREA OF A SQUARE 
len = float (input ("Enter the length of the : "))
area = len**2
perimeter = 4*len
print("Area = ",area, "Perimeter = ",perimeter)

