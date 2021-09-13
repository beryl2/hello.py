# python program to print hello world
print("hello world!")
#related examples (print fibonacci sequence
# a fibonacci sequence is the interger sequence of 0,1, 2, 3, 3 4,5 )
#fibonacci sequence up to the nth term
nterms = int(input("how many terms?"))

#fiirst tow terms
n1, n2 = 0, 1
count = 0 
#check if the number of terms is valid
if nterms <= 0:
    print("please enter a positive integer")
    #if there is only one term, return n1
elif nterms == 1:
    print("fibonacci sequence upto",nterms,":")
    print(n1)
        #generate the fibonacci sequence
else:
    print("fiboncci sequence:")
    while count< nterms:
        print(n1)
        nth = n1 +n2
        #update values
        n1 = n2
        n2 = nth
        count +=1
#python program to print the fibonnacci sequence using recursion    
# the first term are obtained by adding the proceding two terms. this means to say the nth is the sum of n-1 and n-2 term 
def recur_fibo(n):
   if n <=1:
       return n
   else :
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

#check if the number of terms is valid
if nterms <= 0:
    print("please enter a positive integer")
else:
        print("fibonacci sequence:")
        for i in range(nterms):
            print(recur_fibo(i))
#  display the power of two using anonymous function
terms = 10
#uncomment code below to take input from the user
terms = int(input("how many terms?"))
 #use anonymous function
result = list(map(lambda x: 2**x, range(terms)))
print("the total terms are :",terms)
for i in range(terms):
     print("2 raised to power",i,"is",result[i])
#find a number divisible by another number (finding numbersdivisibl by 13)
#ttake list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221]

#use anonymous function to filter 
result = list (filter(lambda x: (x% 13 ==0), my_list))
#display the result
