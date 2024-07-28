# List is basically array
marks = [94.4,54.8,75.3,68.10,92.47]
print(marks,type(marks))

# elements 0f list can be accessible and manipulated  
marks[0]=15
marks[-1]=90
print(marks)

# list slicing
print(marks[1:4])
print(marks[-3:-1])

# unlike an array, a list can carry every type of data including string , int , float altogether
info = ["Kuresh","student","Address"]
print(len(info))

# List methods
array = [12,45,5,9,2]
array.append(16)
print(array)
array.sort() #ascending order
print(array)
array.sort(reverse=True) # descendind order
print(array)


fruits = ["Licchu","Banana","Apple"]
print(fruits)
fruits.sort() # alphabetical sort 
print(fruits) 
fruits.sort(reverse=True)
print(fruits) 

alpha = ['a','b','c','d']
alpha.reverse()
print(alpha)
alpha.insert(2,'f')
print(alpha)
alpha.sort()
alpha.remove('f')
print(alpha)
alpha.pop(1)
print(alpha)

# TUPLES IS SAME AS STRING WHICH IS IMMUTABLE . IT CAN BE ACCESSED BUT CAN'T BE CHANGED

tup =(4,6,81,92,54,92)
print(tup)
print(tup[2])
tup1=()
print(tup1) # it can be empty
print("Slicing of the Tuple: ",tup[-3:-1])
print("Indedx of the Tuple: ",tup.index(92))
print("How many times does a Tuple occur: ",tup.count(92),"\n")


# first question entering the names of movies and store them in a list
#1st way
# movies=[input("Enter First Movie: "), input("Enter Second Movie: "), input("Enter Third Movie: ")]
# print(movies)

#2nd way
# movie = []
# mov1 = input("Enter First Movie: ")
# mov2= input("Enter Second Movie: ")
# mov3= input("Enter Third Movie: ")
# movie.append(mov1)
# movie.append(mov2)
# movie.append(mov3)
# print(movie)

#3rd way
# mov = []
# mov.append(input("Enter First Movie: "))
# mov.append(input("Enter second Movie: "))
# mov.append(input("Enter third Movie: "))
# print(mov)

# CHECKING PALINDROME
menu = [1,2,3,2,1]
copy_menu = menu.copy()
copy_menu.reverse()
if(copy_menu == menu):
    print("Menu is palindrome")
else:
    print("It's not palindrome")
print("     ")

# store the values of tuple in a list and sort the list [c,D,A,A,B,B,A]





