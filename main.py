# p1 program to print hello world
print("hello world!")
# p2 adding two numbers
num1 = 1.5
num2 = 6.3
sum = num1 + num2
print("the sum of {0} and {1} is {2}".format(num1, num2, sum)) 
# p3 add two numbers with user input
num1 =input("enter the first number: ")
num2 =input("enter the second number: ")
sum =float(num1) + float(num2)
print("the sum of {0}and {1} is {2}".format(num1, num2, sum))
#p4 python program to calculate the squareroot
num = 8
num_sqrt = num **0.5
print("the squareroot of %0.3f is %0.3f"%(num, num_sqrt))
# calculate the area of a triangle
a = 3
b = 4
c = 77


# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a+b+c)/2
#calculating area
area = (s*(s-a)*(s-b)*(s-c)) **0.5
print('The area of the triangle is %0.2f' %area)