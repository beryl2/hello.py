#from collections import namedtuple
#from typing import AsyncGenerator


print((2+10)*(10+4))
a=5
print(a)
print(a+a)
a=a*5
#print a
print(a)
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)
#strings (use "double quotes and single quote''  ")
mystring ='abcdegh'
print(mystring[::])
#slicing
mystring.upper()
mystring = 'abcdefg'
x = mystring.capitalize()
print(x)
mystring= "hello world"
x = mystring.split()
print(x)
#print formatting
x="item one: {y} item two:{y}".format(x="dog",y="cat")
print(x)

#list
mylist = [1,2,3]
#mylist = ['stringadgasfd' , 1,2 ,32, 23.3, true[1,2,3,4]]
print(len(mylist))
#indexing and slicing(if you want the very first thing in the list)
mylist = ['a', 'b', 'c']
print(mylist[:3])
#adding items to a list
print('before reassignment:')
print(mylist)
mylist[0] = 'NEW ITEM'
print('after reassignment')
print(mylist)
#basic list method(adding a new items )
mylist = ['a', 'b', 'c', 'd', 'e'] 
mylist.append("NEW ITEM")
print(mylist)
#exttend
mylist = ['a', 'b', 'c', 'd', 'e', ]
mylist.extend(['x', 'y','z'])
print(mylist)
#removing something from a list
mylist = ['a', 'b', 'c', 'd', 'e'] 
item = mylist.pop(0)
print(mylist)
print(item)
#reversing and sorting a list
mylist = ['a', 'b' ,'c', 'd', 'e', 'f', 'g']
mylist.reverse()
print(mylist)
#sorting
mylist = [2, 4 ,1 ,6, 97,76]
mylist.sort()
print(mylist)
#nested list index and 
#nested list
mylist = [1,2,['x','y', 'z']]
print(mylist[2])
#to specify the index
mylist= [1,2, ['x', 'y','z']]
print(mylist[2][1])
#list comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)
#dictionaries
my_stuff = {"key1":"value1","key2":"value2","key3":{'123' :[1, 2, 'grab me']}}
print(my_stuff['key3']['123'][2].upper())
my_stuff = {'lunch':'pizza', 'brakefast':'eggs', 'supper':'ugali'}
my_stuff['lunch'] = "burger"
my_stuff['dinner'] = 'pasta'
print(my_stuff['lunch'])
print(my_stuff)
#tuples ,sets and booleans
#booleans(true or false)or 0 or 1
#tuples are immutables sequences
t= (1, 2, 3, 4)
print(t[0])
mylist = ['a', 'true', '123']
print(mylist)
mylist[0] = 'new'
print(mylist)
#set
x = set()
x.add(1)
x.add(2)
x.add(4)
x. add(3)
x.add(3)
x.add(3)
print(x)
#converting a set into a list
converted = set([1, 2, 3, 1, 2, 2, 3, 4, 5, 3, 6, 6, 6, 6 ])
print(converted) 
#function

#def greet(name):
   # """ this function greet to the person passed in as a parameter""" 
def absolute_value(num):
        if num >= 0:
            return num
        else:
                return -num
print(absolute_value(2))
print(absolute_value(-4))
#scope of a variable insie a function
def my_func():
    x = 10
    print("value inside function:",x)
x=20
my_func()
print("value outside function:",x)
 
def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Monica", "Good morning!")
def greet(name, msg='goodmorning!'):
#"""this function greets to the prson with the provided message
#if the message is not provided it defaults to good morning!"""
 print("hello", name+',' +msg)
greet('kate')
greet("bruce","how do you do?")

3#lass Customer:
 #   def__init__(self, name,membership_type):
  #  self.name = name
   # self.membership_type = membership_type  
    #print("customer created")
#c = Customer("Caleb", "Gold")
#print(c.name, c.membership_type)

#c2 = Customer("brad", "bronze")
#print(c2.name, c2.membership_type)

def greet(name):
    """this function greets to the person passed in as a parameter"""
    print("hello," +name+".good morning!")
greet("paul")
def absolute_value(num):
    if num>= 0:
         return num
    else:
         return -num
print(absolute_value(2))
print(absolute_value(-4)) 
#arbitrary
def greet(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)

#example 2
greet("Monica", "Luke", "Steve", "John")
def greet(*names):
    
    for name in names:
        print("hello", name)
greet("ruth", "jane", "hosea")

#filter function to filter only even numbers from a list
my_list = [1, 2,3,4, 5,6, 7, 8,12]
new_list= list(filter(lambda x:(x%2==0) ,my_list))
print(new_list)
#program to double each item in a ist using map
my_list = [1, 2, 3, 4, 5, 7, 12]
new_list = list(map(lambda x: x*2, my_list))
print(new_list)
#global variable and local variable in the same code
x= "global"
def foo():
    global x
    y="local"
    x = x * 2
    print(x)
    print(y)
foo()
#global vaiable and local variable as the same name
x =5
def foo():
    x =10
    print("local x:", x)
foo()
print("global x:",x)   # mendrygals


c = 1 #global variable
def add():
    print(c)
add()
# (Modifying Global Variable From Inside the Function
#c = 1 #global variable
#def add(): 
    #c = c + 2 #increment with 2
    #print(c)
#add()    
#when we run the above program the output unbound local error because  we can only access the global variable but cannot modify it from side the function
#  Changing Global Variable From Inside a Function using global
c = 0 #global variable
def add():
    global c
    c = c + 2 #increment by two
    print("inside add:", c)
add() 
print ("in main:",c)   
#using global variable in nested function
def foo():
    x = 20
    def bar():
        global x 
        x = 25
        print("before calling bar:", x)
        print("calling bar now")
        bar()
        print("after calling bar:", x)
foo()
print("x in main:", x)
#class description
class parrot:
    #class attribute
    species = "bird"

    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
   # instantiate the parrot
blu = parrot("blu", 10)
woo = parrot("woo", 15)
#access the class attribute
print("blu is a {}".format(blu.__class__.species))
print("woo is also a{}".format(woo.__class__.species)) 
#access the instance attribute
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(blu.name, blu.age))
#methods
class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())


#inheritence
 #parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("swim faster")
#child class
class penguin(Bird):

    def __init__(self):
        #call super() function
        super().__init__()
        print("penguinis ready")
    def whoisThis(self):
        print("penguin")

    def run(self):
        print("run faster")
peggy = penguin() 
peggy.whoisThis()
peggy.swim()
peggy.run()  

#encapsulation
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

def a_void_function():
    a = 1
    b = 2
    c = a + b
x = a_void_function()
print(x)    
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)
a =2
print('id(2) =', id(2))
print('id(a) =', id(a))
#example 2
a = 2
print("id(a) =", id(a))
a = a+1
print("id(a)=", id(a))
print("id(3) =", id(3))
b = 2
print("id(b) =", id(b))
print("id(2) =", id(2))
#if statement
num = 3
if num > 0:
    print(num, "is always a positive number")
print("this is always printed")

num = -1
if num > 0:
    print(num, "is a positive number")
print("this ia also always printed.")
#if else statement
#program checks if the number is positive or negative
#and displays an appropriatenmassage
num = 0
#try these two variation as well
if num >= 0:
    print ("positive or zero")
else:
    print ("negative number")
#if... else.... elif ...else
#  elif is the short form of if else(it allows us chck for multiple expression)
num = 0
#try these two variation as well
# num = 0
# num = -4.5
if num > 0:
    print("positive number")
elif num == 0:
    print("zero")
else:
    print ("negative number")
#nested if ...eli else statement
num = float(input("enter a number: "))
if num >= 0:
    if num == 0:
       print("zero")
    else:
         print("positive number")
else:
    print("negative number")
#a program to find the sum of all stored in a list
# #list of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11] 
#variable to store the sum 
sum = 0
#iterate over the list
for val in numbers:
    sum = sum + val
print("the sum is", sum)
#program to iterate through a list using indexing
genre = ['pop', 'rock', 'jazz']
#iterate over the list using index
for i in range(len(genre)):
    print("i like", genre[i])

#programto display student's mark from record
student_name = 'soyuj'
marks = {"james": 90, "jules": 55, "arthur": 77}
for student in marks:
    if student ==student_name:
        print(marks[student])
        break
else:
    print("no entry with that name foound.")    
#filter even numbers from a list
my_list=[1, 2, 3,4 , 6, 8, 5, 12]
new_list= list(filter(lambda x:(x%2==0), my_list))
print(new_list)
#program to double each tem in a list using map
my_list=[1, 2, 3, 4, 4, 45 , 6 ,11]
new_list=list(map(lambda x: x*2, my_list))
print(new_list)
def myfunc(n):
    return lambda x: x * n
mydoubler = myfunc(2)
print(mydoubler(11))
#use the the same function definition to  double and triple the number you send in
def myfunc(n):
    return lambda x: x*n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
#inheritance

   
  

           
