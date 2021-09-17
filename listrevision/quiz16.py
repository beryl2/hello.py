def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1)) 
num = 10
print("the factorial of", num, "is", factorial(num))
#write a python tring in the middle of a string
#We first use the string.find() method to get the substring index in the string, 
# after which we need to insert another string.
#  After getting the substring index, we split the original string and then concatenate the split strings and the string we need to insert using the + operator to get the desired string.

my_string ='{{}}'
index = my_string.find('}')
final_string = my_string[:index] +'php'+ my_string[index:]
print(final_string)  

                        #Quiz 17
#Python function to get a string made of 4 copies of the last two characters of a specified string   
#take thestring from the user
#intialize a count variable to 0
#use a for loop to transverse through the character in the string and increment count variable each time
#from the new string using string slicing
#print the newly formed string
string = 'python'
count= 0
for i in string:
    count = count+1
new =string[-2:] +string[count-2:count]+string[count-2:count]+string[count-2:count]
print("newly formed string is:")
print(new)    

#User must enter a string and store it in a variable.
# The count variable is initialized to zero.
# The for loop is used to traverse through the characters in the string.
# The count is incremented each time a character is encountered.
# The new string is formed by using string slicing and  the last two letters of the string are concatenated using the ‘+’ operator.
# The newly formed string is printed.

                           #QUIZ 18

#function to get a string made of its first three characters of a specified string. 
#If the length of the string is less than 3 then return the original string
str = 'python'
def last_three(str):
    if len(str)<3:
        return 'python'
    return str[0:4] 
print(last_three('py'))
print(last_three('pth'))  
                      #quiz19
#Python program to get the last part of a string before a specified character.

                     #Quiz20
#function to reverses a string if it's length is a multiple of 4                     
str= input("enter a string: ")
if(len(str)%4==0):
    print(str[::-1])
else:
    print("cant")    