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
l2 = f.readline()
print(l1)
print(l2)
f.close()