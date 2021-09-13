#exercise review
#given a string 

#use indexing to print out the following
#'d'
s = 'django'
print(s[0])
#'o'
s = 'django'
print(s[-1])
# 'djan'
s = 'django'
print(s[:4])
#'jan'
s = 'django'
print(s[1:4])
#'go'
s = 'django'
print(s[4:])
#use indexing to reverse the string
s = 'django'
print(s[::-1])
#given this nested lists.
#l =[3,7,[1,4,'hello']]
#reassign "hello" to be "goodbye"
l = [3,7,[1,4,'hello']] 
print(l)
l[2][2]= 'goodbye'
print(l)
#using keys and indexing ,grab the hello from the following dictionaries
d1 = {'simple_key':'hello'}
print(d1['simple_key'])
#2
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
#3
d3 = {'k1' :[{'nesty_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nesty_key'][1][0])
#problem 4(use a set to find the unique vakues of the list below)
mylist = [1,1,1,1,1,1,2,2,22,2,2,3,3,3,3,3]
print(set(mylist))
#you are given the following variable
age = 4
name = "sammy"
#use print formatting to print the following strings
#"hello my dog's nam is sammy he is 4 years old"
print("hello my dog's name is {a} he is {b} years old". format(a=name, b=age))
#program to swap two variable
x = 5
y = 10
#to take input from the user
#x = input("enet vale of x: ")
#y =  inpt("enter value of y: ")
#create a temporary variable and swap the values
temp = x
x = y
y = temp
print("the value of x after swapping: {}".format(x))
print("the value of y after swaooing: {}".format(y))
#include a random number in the range o to 9
#import a random module
import random
print(random.randint(0,9))



#python program to shuffle a deck of card
#import modules
import itertools, random
#make a deck of card
deck = list(itertools.product(range(1,14),["spade", "heart","diamond","club"]))

#shuffle the cards
random.shuffle(deck)
#dra five cards
print("you got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])


#converting kilometer to miles
kilometer = float(input("enter value of the kilometers: "))


#conversion factor
conv_fac = 0.621371

#calculate miles
miles = kilometer* conv_fac
print("%0.2f kilometer is equal to %0.2f miles" %(kilometer,miles))



#program to convert temperature in celsius to fahrenhiet
celsius = 37.5

#calculate fahrenheit
fahrenheit = (celsius * 1.8) +32
print("%0.1f degree celsius is equal to %0.1f fahrenheit"%(celsius, fahrenheit))


#print each statement on a new line
print("python")
print("is easy to lern.")
#this create a new line
print()

#print both statement in a single line
print("python", end="")
print("is easy to learn.")

print()
num = float(input("enter the number: "))
if num >0:
    print("positive number")

elif num ==0:
    print("zero")

else:
    print("negative number")

#python program checking if the number is even or odd
num = int(input("enter the number: "))
if (num%2) == 0:
    print("{0} is even".format(num))
else:
    print("{0} is odd".format(num))    

#program finding a leap year
year = 2000

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap yaer".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year) ) 

#program to find the largest number among three input
num1 = 10
num2 = 14
num3 = 12
if (num >= num2) and (num1 >=num3):
    largest = num1
elif (num2 >=num1) and (num2 >=num3):
    largest = num2
else:
    largest = num3
print("the largest number is", largest)


#checking of prime numbers
#num = 29

#define the flag variables
#flag = False

#prime numbers are greater than one
#if num > 1:
    #check for factors
    #for i in range(2, num):
       # if (num % i) == 0:
            #if factor is fond, set flag to true
           # flag = True
            #break out of loop
           # break

#check if flag is true
#if flag:
    #print(num, "is not a prime number")
#else:
 #   print(num, "is a prime number")


 #python program to find a squareroot
num = 34

#to find the squareroot
num_sqrt = num ** 0.5
print("the squareroot of %0.3f is %0.3f"%(num, num_sqrt))

#example two (squareroot for a negative number and complex number)
import cmath
num = 1 +2j
num_sqrt = cmath.sqrt(num)
print("the squareroot of {0} is {1:0.3f}+{2:0.3f}j".format(num,num_sqrt.real,num_sqrt.imag))


#python program to print a number to print all program on an interval
print()
print()
#program to find the factorial of a number
num = 7
factorial = 1
if num < 0:
    print("factorial does not exist for neegative number")
elif num == 0:
    print("the factorial of 0 is 1")
else:
     print("the factorial of" ,(num),"is", factorial) 

#display the multiplication table
num = 12
for i in range(1, 12):
    print(num, "x", i, "=", num*i)






#check if a number is an armstrong ornot
num = int(input("enter the number: "))
#initialize sum
sum = 0
#find sum of the cube in each digit
temp = num
while temp >0:
    digit = temp % 10
    sum += digit **3
    temp //= 10
#display sum
if num ==sum:
    print(num, "is a armstrong number")
else:
    print(num,"is not an armstrong number")       



        


                             

      


