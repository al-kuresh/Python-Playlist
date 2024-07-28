#3 WAYS TO WRITE DOWN A STRING IN PYTHON
str = "Hi,  I am Al  kuresh"
str1 = 'Kuresh' #single qoutation for a word
str2 = """Hello from the outside""" #triple qoutation for sentence
print(str)
print(str1)
print(str2)

#Escape Sequence \n , \t
str3="hello world.\nHow are you"
print(str3)

#Concatenation
word1 = "I Love"
word2 = " You"
print(word1+word2)

#Length 
word3= word1+word2
print(len(word3))

#Indexing
state= "Kuresh Reush"
char = state[7]
print(char)

#slicing
state= "Kuresh Reush"
print(state[2:len(state)])
print(state[2:5])

#String Functions
state= "akuresh Reush"
print(state.endswith("kur")) # checks the ending of the string and returns true/false value 
print(state.capitalize())   # it change the first alphabet of the string to capital from small letter but it works only one time while printing
print(state)                # akuresh reush the a hasn't changed yet here
state = state.capitalize()  # Now it is permanently changed from akuresh reush to Akuresh reush
print(state)

sen = "I am learning Python for Artificial Intelligence"
print(sen.replace("a","K")) # It replaces the all 'a's of the string into 'K's
print(sen.replace("Python","Java"))
print(len(sen))
print(sen.find("I"))
print(sen.count("a"))

# WAP TO INPUT USER'S FIRST NAME  AND PRINTS IT'S LENGTH

# name = input("Enter your First name: ")
# print(len(name))

# # CONDITIONAL STATEMENTS if elif else
# light = input("Enter the Signal: ")
# if(light == "Green" or "green"):
#     print("Go")
# elif(light == "yellow" or "Yellow"):
#     print("Pause")
# else:
#     print("Stop")

# 2ND PROGRAM OF IF ELSE
# marks = float (input("Enter your marks: "))

# if(marks>=90):
#     print("Grade is : A")
# elif(marks<90 and 80<=marks):
#     print("Grade is : B")
# elif(marks<80 and 70<=marks):
#     print("Grade is : C")
# elif(marks<70  and 60<=marks):
#     print("Grade is : D")
# else:
#     print("Fail")
# print("     ")

# # odd and even
 
# number =  int (input("enter number: "))
# if(number%2==0):
#     print("Number",number,"is even")
# else:
#     print("Number",number,"is odd")
# print("     ")
               
# # Greatest of 3 numbers
# a= float(input("Enter A= "))
# b= float(input("Enter B= "))
# c= float(input("Enter C= "))

# if(a>=b and a>=c):
#     print(a,"is the greatest Number")
# elif(b>=a and b>=c):
#     print(b,"is the greatest Number")
# else:
#     print(c,"is the greatest Number")
# print("     ")

# Multiple of 7
num = int(input("Enter value: "))
if(num%7==0):
    print(num,"is a multiple of 7")
else:
    print(num,"is not a multiple of 7")
print("     ")

