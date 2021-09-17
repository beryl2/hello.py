#write a program to calculate the length of a string
str = "welcome home"#here space is also counted as part of the lengthstring
print(len(str))

print()

#write a program to count the number of character frequency in a string

#dictionary(keys and values)
#iteration

print() 
str = "google.com"
all_freq = {}
for i in str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("count of all characters in google.com is", (all_freq, str))            

#write a program to get a string made of the first 2 and the last 2 char from a given string
#if the string is less than two char instead return an empty list
str = "w3resource"
def string_both_ends(str):
    if len(str)<2:

        return("empty string")

    return str[0:2] +str[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends("w3"))
print(string_both_ends('w'))

#write a program to get a single string from a given string where alll occurence have been changed to $
#expected result: resta$t
def change_char(str):
    char = str[0]
    str = str.replace(char,'$')
    str = char+str[1:]
    return str
print (change_char('restart')) 

#a program .to add ing at the end of a given string.if the sting ends with an ing then repelce it with an ly
def addprefix(s):
    if len(s)<3:
        return s
    else:
        if s[-3:] !="ing":
            return s+"ing"
        else:
            return s+'ly'
s = input('enter the string: ')
s1=addprefix(s)
print("after adding suitable prefix:", s1)            


#a program to find the first appearance of a substring "not" and "poor"
#if not follows the poor replace the substing 'good'
def not_poor(str1):
    snot = str1.find('not')
    spoor =str1.find('poor')
    if spoor >snot and snot>0 and spoor>0:
        str1 = str1.replace(str1[snot:spoor+4], 'good') 
    else:
       return str1
print(not_poor('the lyrics is not that poor!'))
print(not_poor("the lyrics is poor!")) 

#write a program that takes a list
#return the longest word and the length of the longest one

word = "excercise"
print(len(word))

# python program to remove the nth index character from a nonempty string
#Take a string from the user and store it in a variable.
# Take the index of the character to remove.
# Pass the string and the index as arguments to a function named remove.
# In the function, the string should then be split into two halves before the index character and after the index character.
# These two halves should then be merged together.
# Print the modified string.
 
def remove(string, n):
    first = string[:n]
    last = string[n+1:]
    return first +last
string =input("enter the string: ")
n=int(input("enter the index of the character to remove: "))
print("modified string: ")
print(remove(string, n))

#Write a Python program to change a given string to a new string 
#where the first and last chars have been exchanged.:
   #program takes the a string and swap the first character and the last character of the string
   #take a string from a user and store it in a variable
   #pass the string as an argument to a function
   #in the function split the sting
   #add the last charater to the middle part of the string which is in turn added to the first character
    #print the modified string
def change(string):
    return string[-1:] +string[1:-1] +string[:1]
string = input("enter string: ")
print("modified string:")
print(change(string))


#program to change a given string to a new string where the last two char have been changed
#Take a string from the user and store it in a variable.
# Pass the string as an argument to a function.
# In the function, split the string.
#Then add the last character to the middle part of the string which is in turn added to the first character.
# Print the modified string.

def new(string):
    return string[-1:] +string[1:-1] +string[:1]
string= input("enter string: ")
print('modified string:')
print(change(string))  

   #    QUIZ 11
#program to remove the characters which have odd index values of a given string.
def remove_odd(string):
    result = ""
    for i in range(len(string)):
        if i %2==0:
            result = result+ string[i]
    return result
string=input("enter string:")
print("modified string is")
print(remove_odd(string))   

#User must enter a string and store it in a variable.
# This string is passed as an argument to a function.
# In the function, a variable is initialized with an empty character.
# A for loop is used to traverse through the string.
# An if statement checks if the index of the string is odd or even.
# If the index is odd, the empty character variable is appended to the string thus indirectly removing the character.
# Finally the modified string is printed.

            #QUIZ 12

# Python program to count the occurrences of each word in a given sentence

#Take a string and a word from the user and store it in separate variables.
# Initialize a count variable to 0.
# Split the string using space as the reference and store the words in a list.
# Use a for loop to traverse through the words in the list and use an if statement to check if the word in the list matches the word given by the user and increment the count.
# Print the total count of the variable.

string= input("enter string: ")
word= input("enter word: ")
a= []
count = 0
a=string.split(" ")
for i in range(0,len(a)):
    if(word==a[i]):
        count= count+1
print("count of the word is: ")
print(count)    

#User must enter a string and a word and store it in separate variables.
# The count variable is initialized to zero.
# The string is split into words using space as the reference and stored in a list.
# The for loop is used to traverse through the words in the list.
#The count is incremented each time the word in the list is equal to the word given by the user.
# The total count of the word is printed.


            #QUIZ13
#Python script that takes input from the user and displays that input back in upper and lower cases.            
str=(input('enter sting: '))
print(str.upper())


             #QUIZ 14     
#Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)

#Take a hyphen separated sequence of words from the user.
# Split the words in the input with hyphen as reference and store the words in a list.
# Sort the words in the list.
# Join the words in the list with hyphen between them and print the sorted sequence.
print("enter the comma separated list sequene of words: ")
list=[n for n in input().split(",")]
list.sort()
print("sorted:")
print(",".join(list))

#Take a hyphen separated sequence of words from the user.
# Split the words in the input with hyphen as reference and store the words in a list.
# Sort the words in the list.
# Join the words in the list with hyphen between them and print the sorted sequence.

            #QUIZ 15
#Python function to create the HTML string with tags around the word                       
def add_tags(tag, word):
    return '<%s>%s</%s>' %(tag, word, tag)
print(add_tags('i', 'python'))  
print(add_tags('b','python tutorial')) 

              #greet function
def greet(name):
    print("hello," +name+ "goodmorning")              
greet('paul')    




