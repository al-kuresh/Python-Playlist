# Number 1
#Creating Class

class Cars:
     name = "Mercedes"
     number = 456

#Creating Object instances
c1 = Cars()
print("Car Name  : ",c1.name)
print("Car Number: ",c1.number)

# Number 2
#creating constructor
class Students:
     # Default constructor
     def __init__(self):
          print("Default Const") # won't be printed beacause all the objects have paramters in there constructor

     department  = "ECE"  # this attribute doesn't need to be in the constructor cause it is same for all the students of ECE dept .
                          # that's why department is a class attribute (we can write Students.department instead of s1 or s2.department)   
     # Parameterized Constructor
     def __init__(self,name,id,cgpa):
          self.name = name
          self.id = id
          self.cgpa = cgpa
          # those attributes which are attached to self parameter is called instance attributes
     def grettings(self):
          print("Welcome Students")
        

# data stored in the Objects or variables are Attributes Like Kuresh,2221987,3.79, these three are attributes
s1 = Students("Kuresh",2221987,3.79,)
s1.grettings()  # method is called
print(s1.name," ",s1.id," ",s1.cgpa," ",s1.department)

s2 = Students("Faruque",2221988,3.65)
print(s2.name," ",s2.id," ",s2.cgpa," ",s2.department,"\n")


# Class using method 
class Exam():
     exam_name = "Math"
     def __init__(self,name,marks):
          self.name = name
          self.marks = marks
     def get_marks(self):
          return self.marks
     def Name(self):
          print("Hello ",self.name)

e1 = Exam("Hridoy",85)
e1.Name()
print(e1.get_marks())

# First Question
"""class Student:
     def __init__(self,name,math_marks,phy_marks,chem_marks):
          self.name = name
          self.math = math_marks
          self.phy = phy_marks
          self.chem = chem_marks

     @staticmethod      # Decorator = no need to put the self parameter
     def varsity():     
          print("North South University")
     def average(self):
      print("Average of 3 subjects: ","%.2f" % float(((self.math+self.phy+self.chem)/3)))  # "%.2f" %

s1 = Student(input("Enter name: "),float(input("Enter Math marks: ")),float(input("Enter Physics marks: ")),float(input("Enter Chemistry marks: ")))
print(s1.name)
s1.varsity()
s1.average() """
print("\n")

# 2nd Question
class Bank:
     def __init__(self,account_no,balance):
          self.acc = account_no
          self.bal = balance

     def credit(self,x):
          self.bal= self.bal + x
          print("Current Balance after credit: ",self.bal)

     def debit(self,x):
          self.bal= self.bal - x
          print("Current Balance after debit: ",self.bal)
          
     def balance(self):
          print("Current Balance: ",self.bal)
     
b1 = Bank(1510601997,22000)
b1.balance()
b1.credit(5000)
b1.balance() 
b1.debit(7000) 

b2 = Bank(1510602000,8000)
b2.credit(4000)
b2.debit(2000)
print("\n")

# Public And Private
class Facebook:
     def __init__(self,username,password):
          self.usr = username
          self.__password = password # self.__password here the under score has made the attribute private. that's why it can't be accessed
     def reset_pass(self):
          print(self.__password)

f1 = Facebook("Al_Kuresh","mastermind")
print(f1.usr)
f1.reset_pass()

class person:
     __name = "Kureshreushs"

# this is how we print the private attributes by calling the private method inside a public method 
     def Name(self):
          self.__say_hi()
          print(self.__name)

     def __say_hi(self):
          print("hi")

p1 = person()
# print(p1.__name) invalid cause private attribute __name
# p1.__say_hi()     invalid cause private method __say_hi()
p1.Name()

# Inheritence
# Single Inheritence

class Car:          # Here class car is the parent class and it's methods are needed to static to access them
     @staticmethod            
     def color():
          print("black")
     @staticmethod
     def accelerate():
          print("Car is accelerated")
     

class Lexus_Car(Car):          # Here Lexus_Car() is the child class which is inheriting the methods and attributes of Car class by Lexus_Car(Car)
     def __init__(self,name):
          self.name = name

     def printing(self):
          print("Car name is ",self.name)

c1 = Lexus_Car("LC 500")
c2 = Lexus_Car("Land Cruiser")

c1.printing()
c1.accelerate()
c1.color()
print("\n")

# MUlti_level Inheritence
print("\n")

class Cars:
     def __init__(self,num_plate,reg):
          self.np = num_plate
          self.reg = reg
     def number_plate(self):
           print( "Number plate is",self.np)  
     def registration(self):
          print("Registration is",self.reg)  

# Intermediate class inheriting from Cars
class Brand(Cars):
     def __init__(self,brand_name,num_plate,reg):  
          super().__init__(num_plate,reg)
          self.brand = brand_name
     def brandName(self):
          print( "Car brand is",self.brand)

# Derived class inheriting from Brand(Cars) (multi-level inheritance)
class Type(Brand):
     def __init__(self,brand_name,num_plate,reg,type):
          super().__init__(brand_name,num_plate,reg)
          self.type = type
     def car_Type(self):
          print( "Car Type is",self.type)

# Creating an object of the Type class
c3 = Type("Audi","B45-012",14986,"Hybrid")

# Calling methods from all levels of inheritance
c3.brandName()
c3.number_plate()
c3.registration()
c3.car_Type()
print("\n")

# Multiple Inheritence 

class Person_A :
     rel_A = "Al Kuresh"
class Person_B:
     rel_B = "Bobby" 

class Person_C(Person_A ,Person_B):
     def relation(self):
          print("Kuresh And Bobby are Brothers")  

Pc = Person_C()
print(Pc.rel_A) 
print(Pc.rel_B)
Pc.relation()

print([1,2,3]+[4,5,6])

# dunder function (double underscore) __

class complex:
     def __init__(self,real,img):
          self.r = real
          self.i = img

     def showNUm(self):
          print(self.r,"+",self.i,"i")

     def __add__(self,other):     # Operator overloading
          newR = self.r + other.r
          newI = self.i + other.i
          return complex(newR,newI)


c1 = complex(4,5)
c2 = complex(3,10)
c3 = c1+c2
c3.showNUm()