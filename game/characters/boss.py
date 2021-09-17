#program to add two matrices
from tkinter.constants import Y


X = [[12,7,3],
    [4, 5, 6],
    [7, 8, 9]]


Y =[[5,8,1],
     [6,7,3],
     [4,5,9]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]    

#iterate throw rows
for i in range (len(X)):
      #iterat through columns
     for j in range (len(X[0])):
          result[i][j] = X[i][j] + Y[i][j]

for r in result:

     print(r)  

#program that calculate the length of a string
str = "education"

print(len(str))



str = "w3resource"
def string_both_ends(str):
     if len(str) < 2:
          return"empty string "

     return str[0:2] + str[-2:]


print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

#program key
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))

#program to change the occurence of the first characer to $ except from the first character
str = ('restart')
def change_char(str):
     char =str[0]
     str = str.replace(char, "$")
     str = char + str[1:]
     return str
print(change_char('restart')) 

#program to add "ing" at the end of a given string .and for a strinfg that ends p with ing add an 'ly'instead
str1 = 'abc'
str2 = 'ing'

str3 = str1.__add__(str2)
print(str3)
#program adds ly to a string end with ing
string = input()
if len(string)< 3:

     print (string)
elif str[-3:] =='ing':
     print (string +"ly")
else:

     print(string + 'ing')


x =[ ]
for x in range (1499, 2701):
     if ((x%5==0) and (x%7==0)):
          print("",x)

          
print()

#python program to revese a number
n = 35231
rev = 0
while(n > 0):
     a = n%10
     rev = rev *10 + a
     n = n // 10
print(rev)

def _sum(arr):
     sum = 0
     for i in arr:
          sum =sum + i 
          return(sum)
     arr = []
     arr [12, 4, 3, 15]  

     n =len(arr) 

     ans = _sum(arr)

     print('sum of the array is', ans)          



     









  



              