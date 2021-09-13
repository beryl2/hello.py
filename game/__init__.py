#display a product of two using anonymous function
terms = 10
#use ananymous function
result = list(map(lambda x:2 ** x, range(terms)))
print ("the total terms are:", terms)
for i in range(terms):
    print("2 rased to poweer", i, "is", result[i])  
    #program to find the sum of natural numbers
    num = 16
    if num < 0:
        print("enter a positive number")
    else:
        sum = 0
        #use while looop to iterate until zero
        while num < 0:
            sum += num
            num -= 1
            print('the sum is', sum)



            #question one


#python program to find a number divisible by another number
#take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221]
#use anonymos function to filter
result = list(filter(lambda x: (x%13 == 0), my_list))

#display the result
print("number divisible by 13 are", result)



            #question two


#program to convert decimal into other number SystemError
dec = 344
print("the decimal value of",dec, "is:")
print(bin(dec), "in binary")
print(oct(dec),"this is octal")
print(hex(dec),"in hexadecimal") 
    


            #QUSTION THREE

#python program to find h.c.f of two numbers

#define a function
def compute_hcf(x, y):
    #choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
num1 = 54
num2 = 24
print("the H.C.F. is", compute_hcf(num1,num2))

            #QUSTION FOUR
#python program to find HCF or gcd

def compute_hcf(x, y):
    #choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range (1, smaller+1):
        if ((x % i == 0) and (y % i ==0)):
            hcf = 1
            return hcf
num1 = 54
num2 = 24     
print("the H.C.F is", compute_hcf(num1, num2)) 

          #QUESTION FIVE
#pyton program to find lcm of two input numbers
def compute_lcm(x, y):
    #choose the greater number
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x ==0) and (greater % y ==0)):
            lcm = greater
            break
        greater += 1

    return lcm

num1 = 54
num2 = 24
print("the lcm is", compute_lcm(num1,num2))
#program to find a factor of a number
#this fuction computes the factor of the argument
def print_factors(x):
    print("the factor of",x,"are:")
    for i in range(1, x + 1):
        if x % i ==0:
            print(i)
num =320
print_factors(num)  

#program that makes a simple calcultor
#this function adds two numbers
#
#program to display calendar
#import calender module
import calendar

yy = 2014 #year
mm = 11 #month


#display the calendar
print(calendar.month(yy, mm))



               


        


