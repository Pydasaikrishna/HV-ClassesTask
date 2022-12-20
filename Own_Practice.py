#================Conversions===================
#decimal to Binary
# sai = bin(25)
# print(sai)


#decimal to octal
# sai = oct(25)
# print(sai)


#decimal to hexa
# sai = hex(25)
# print(sai)


#binary to octal
# sai = oct(0b101)
# print(sai)


#================ Swaping the Values ==============
# a=5
# b=6

# temp =a
# a=b
# b=temp
# print(a)
# print(b)



# a=5
# b=6

# a=a^b
# b=a^b
# a=a^b
# print(a)
# print(b)



# a=5
# b=6

# a,b = b,a
# print(a)
# print(b)



# ==================Bitwise operators====================

# completement - ~ 
# s = ~12
# print(s)    #2's complement means converting into binary and 1's complement+1

# s = ~45
# print(s)


#bitwise AND,OR
#AND
# s = 12&13
# print(s)

#OR
# s = 12|31
# print(s)

#EX-or
# s = 12^13
# print(s)

#left shift
# s = 12<<13
# print(s)

#right shift
# s = 12>>13
# print(s)


# ==================import Math=====================

# import math    #inbulit function
# x = math.sqrt(25)  #square root
# print(x)

#floor - going to downward means floor
# import math
# print(math.floor(2.9))   #output-2

#ceil - going upward value
# import math
# print(math.ceil(2.1))   #output-3

#factorial - !
# import math
# print(math.factorial(5))

#power - ^
# import math
# print(math.pow(3,2))

# Pi - constant value
# import math
# print(math.pi)

#simplifying the math as 'm'
# import math as m
# s = m.sqrt(25) 
# print(s)


# =====================Printing Char===============
# ch = input("Enter char: ")
# print(ch[:2])

# ch = input("Enter char: ")[0]
# print(ch)

#==============Evaluating input===========
# result = eval(input("enter exp: "))
# print(result)

#=================giving the input in terminal=========
# import sys
# x=int(sys.argv[1])
# y=int(sys.argv[2])
# z=x+y
# print(z)


# ===========if,if else,elif,nested if=======================
# if False:
#     print("it is right")
#     print("bye")

# x= 2
# r= x%2
# if r==0:
#     print("it is even")
# else:
#     print("bye")


#===============Loops========================
#while loop

#----------printing name several times--------
# i=1   #initialization
# while i<=5:  #condition
#     print("sai",i)
#     i=i+1   #increment

# i=5   #initialization
# while i>=1:  #condition
#     print("sai",i)
#     i=i-1   #decrement

#for loop
# -----------printing line by line-------------
# x=['sai',5,4]
# for i in x:
#     print(i)

#---------printing the numbers in increment order-------
# for i in range(10,20,2): #2 is iteration
#     print(i)

# --------printing the numbers in revese order----------
# for i in range(20,10,-2): #-2 is iteration
#     print(i)

#----------printing numbers except number divisible by 5-----
# for i in range(1,10):
#     if(i!=5):
#      print(i)


#===============Break,Continue,Pass=============
#---------break statement---------
#Break means stop executing the code 
# x = int(input("Enter the candies: "))
# av = 5
# i=1
# while i <= x:
#     if(i>av):
#         break

#     print("Candy")
#     i=i+1
# print("No more candies,bye!!!!!!!!")


#------------Continue statement-------
# Continue means skipping the if statement in code and run remaining code
# for i in range(1,20):
#     if (i%3==0 or i%5==0):
#         continue
#     print(i)

#-----------Pass statement-------------
# pass statement means passing the statement to not work 
# for i in range(1,20):
#     if(i%2!=0):
#         continue
#     else:
#         print(i)


# stopped in class number 22
# have to continue in class 23


