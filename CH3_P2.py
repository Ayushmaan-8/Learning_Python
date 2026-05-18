# import datetime

# Name = input("enter your name :")

# letter = '''
# Dear <|"Name"|>,
# You are selected!
# <|"Date"|>
# '''

# print ("letter")

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print ( letter.replace("Name","baba").replace("Date","18/05/26"))