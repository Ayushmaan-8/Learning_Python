# a = int(input("enter your number : " ))
# for i in range( 1, 11 ):
#     print(a,'X',i,'=',a*i)
  
# i = 1
# while i < 11:
#     print(f"{a} X {i} = {a*i}")
#     i += 1 #i = i + 1 

# Lesson = no intentation needed in range obv and 
# =+ assigns the right side value(+ive) to be the valve of var 
# but += adds the right side value to the actual assigned value of var 

# if(name.startswith()): [startswith conditional value]  


"""Write a program to find whether a given number is prime or not."""
# a = int(input("enter your number : "))
# for i in range(2, a):
#     if (a%i)==0:
#         print(f"The number {a} is not prime ")
#         break
# else:
#     print(f"this number {a} is prime: ") 

'''Write a program to find the sum of first n natural numbers using while loop.''' 
# n = int(input("enter your number : "))
# i = 1
# sum = 0
# while n>=i:
#     sum += i 
#     i += 1 

# print(f"sum of first {n} natural numbers is : ", sum )

# # while n>=0:
# #     c= (n*(n+1))/2
''' this enters infinte loop of printing as there's 
 no end to the while loop the condition never becomes false 
 and no use of this formula is logical, as the formula itself solves the problem and then there's no use of while loop '''

# NOTE = Try making the logic using simpler way for solving the problem like you'd explain it to a 5 year old 

'''Write a program to calculate the factorial of a given number using for loop.'''

# f = int(input("enter your number : "))
# a = 1  
# for i in range (1,f+1):
#     a = a*i 
# print(f"factorial of {f} is {a}") 

# f = int(input("enter your number : "))
# for i in range (1,f+1):
#     print(" "* (f-i), end="")
#     print("*"* (2*i-1), end="")
#     print("") 

# f = int(input("enter your number : "))
# for i in range (1,f+1):
#     print("*"* (i), end="")
#     print("") 

# f = int(input("enter your number : "))
# for i in range (1,f+1):
#     if ( i==1 or i==f):
#         print("*"* (f), end="")
#     else:
#         print("*", end="")
#         print(" "*(f-2), end="")
#         print("*", end="")
#     print("") 

f = int(input("enter your number : "))
for row in range (1,f+1):
    if ( row%2 !=0 ):
        print("*"* (f), end="")
    else:
        for col in range (1,f+1):
            if col % 2 !=0:
                print("*", end="")
            else:
                print(" ", end="")
       
    print("") 