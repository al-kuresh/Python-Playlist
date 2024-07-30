# # Function of printing
# def Printing():
#     print("Hello")




# # Function of Sum 
# def Sum(a,b):  # a,b are the parameters here
#     sum = a+b
#     return sum

# a= int (input("Enter value1: "))
# b= int (input("Enter value2: "))
# print(Sum(a,b)) # a,b are the arguments here

# Printing() # it prints "Hello" cause , we are calling the function
# v = Printing() #storing the value of a printing function gives us none value beacuse it returns nothing
# print(v) # the printing function is not returning anything thats why it prints none
# print("   ")

# # Average of  3 Numbers
# def avg(a,b,c):
#     return ((a+b+c)/3)

# a= float (input("Enter value1: "))
# b= float (input("Enter value2: "))
# c= float (input("Enter value3: "))
# print("Average of 3 numbers: ",avg(a,b,c))


# length of a list 
def length(list):
    return len(list)

# Printing list in one Single line
def print_single(list):
    for i in list:
        print(i,end=" ")

nums   = [4,5,6,7,8]
cities = ["Dhaka","Sylhet","Khulna","Cumilla"]
print("Length of nums",length(nums))
print("Length of cities",length(cities))

print_single(nums)
print("\n")
print_single(cities)
print("\n")

# Factorial of n

def Fact(n):
    fact =1
    for num in range(1,n+1):
        fact*=num
    return fact

f = int (input("Enter num to factorial: "))
print("Factorial of",f,"is",Fact(f))

# Currency Conversion

def convert_to_BDT(dollar):
    return dollar*117.67

dolr = float (input("Enter the amount of Dollar: "))
print("From $",dolr,"to =",convert_to_BDT(dolr),"BDT")