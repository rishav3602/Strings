"""
Write a program to print the letter template given below with name and date.
letter = 
            'Dear |<NAME>|
            You are selected ,
             |<DATE>|'

"""

letter = '''      Dear |<NAME>|
            You are selected ,
              date : |<DATE>| '''
name = input("Enter your name : ")
date = input("Enter your date : ")
letter = letter.replace("|<NAME>|" ,name)
letter = letter.replace("|<DATE>|" ,date)
print(letter)
             