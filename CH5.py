
# 1) Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
# a = {  "sambhav": "possible",
#         "upyog": "usage",
#         "ank": "marks/number",
#         "kagaz": "paper"
#  }
# print( "sambhav,upyog,ank,kagaz" )
# b = input("choose the word to know it's meaning :  ",)
# print(a.get(b))

# 2)Write a program to input eight numbers from the user and display all the unique numbers (once).
a= input("enter the 8 numbers: ")
numbers = set(map(int, a.split()))
print( numbers )