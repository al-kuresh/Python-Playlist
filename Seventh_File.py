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