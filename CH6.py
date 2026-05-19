# """Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user"""
# marks3 = int(input("Enter your marks in subject 3: "))
# marks1 = int(input("Enter your marks in subject 1: "))
# marks2 = int(input("Enter your marks in subject 2: "))
# total_percentage = ((marks1+marks2+marks3)/300)*100
# if ( total_percentage >= 40.0 and marks1>33.0 and marks2>33.0 and marks3>33.0):
#     print("Student passed with overall percentage being",total_percentage)
# else:
#     print("Student failed over all",total_percentage)    

# """A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams."""

# a1="Make a lot of money"
# a2="buy now"
# a3="subscribe this"
# a4="click this"

# comment=input("enter your comment : ")
# if ((a1 in comment)or(a2 in comment)or(a3 in comment)or(a4 in comment)):
#     print("this is spam")
# else:
#     print("You posted your comment: ", comment)    

# in keyword can be used in list and string 

# marks = int(input("Enter your marks for grade : "))
# if ( marks <= 100 and marks >= 90):
#     grade="EX"
# elif ( marks <= 90 and marks >= 80):
#     grade="A"
# elif ( marks <= 80 and marks >= 70):
#     grade="B"
# elif ( marks <= 70 and marks >= 60):
#     grade="C"
# elif ( marks <= 60 and marks >= 50):
#     grade="D"
# else:
#     grade="F"
# print("Your grade is ", grade) 

i = 1
while i < 51: # print "Harry" - 5 times!
 print(i)
 i = i + 1
