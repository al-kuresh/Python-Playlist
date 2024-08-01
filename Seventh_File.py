# f = open("File_name","mode")
# Modes 
"""
"r" for reading a file
"w" for overwrite the file and write new things
"a" for append ( writing in a existing file from the last input)
"x" for creating a new file and write it
"b' for binary mode (rb,wb,ab)
"+" for reading and writing both (r+,w+,a+)
"""

# f.read() reads the entire file
# f.readline() reads the one line at  a time

f  = open("D:\Python Folder\prototype.txt","r")
text = f.read()
print(text)
f.close()

print("\n")

f =open("D:\Python Folder\prototype.txt","r")
text1  = f.read(10) # read the first 10 characters of the file
print(text1,"\n")
f.close()

f =open("D:\Python Folder\prototype.txt","r")
l1 = f.readline() # reads the first whole line of the file
l2 = f.readline() # reads the second whole line of the file
print(l1)
print(l2)
f.close()

# Writing something in a file
f = open("D:\Python Folder\prototype.txt","w")
f.write("The next thing I am going to learn is Html and Css")
f.write("\n123")
f.write("\nDjango as well")
f.close()

# Appending in a file
f = open("D:\Python Folder\prototype.txt","a")
f.write("\nThen I will proceed to a project")
f.close()

#Reading the entire file again
with open("D:\Python Folder\prototype.txt","r") as f:
    doc = f.read()
    print(doc)

with open("D:\Python Folder\prototype.txt","w") as f:
    f.write("we use the with function")

# removing a file from folder by importing built in library Operating System  (os)
# import os
# os.remove("D:\Python Folder\sample.txt")

# Files related Question 
with open("D:\Python Folder\practice.txt","w") as f:
    f.write("Hi everyone\n")
    f.write("We are learning File I/O\n")
    f.write("Using Java\n")
    f.write("I like Programming in Java\n")

# Replacing any words in the practice file
def rep(word1,word2):
     with open("D:\Python Folder\practice.txt","r") as f:
        value= f.read()
        new_value = value.replace(word1,word2)
        print(new_value)
        return new_value

word1 = input("Enter word: ")
word2 = input("Enter word: ")
new_value=rep(word1,word2) 



with open("D:\Python Folder\practice.txt","w") as f:
     f.write(new_value)


#Searching an word in file through file an function
def search(ser):
 with open("D:\Python Folder\practice.txt","r") as f:
    sen = f.read()
    word = sen.find(ser)
    if(word!=-1):
         print("found")
    else:
         print("Not found")

ser = input("Enter word: ")
search(ser) 

# Searching the line number in a file
def lin_serc(word):
    with open("D:\Python Folder\practice.txt","r") as f:
        count=0
        sentence = True
        found = False
        while sentence:
         sentence = f.readline()
         count+=1
         if(sentence.find(word)!=-1):
            print(word,"is in Line number",count) 
            found =True
    return found
        
words = input("Enter word: ")
checker=lin_serc(words)
if(checker == False):
    print(checker)
    
