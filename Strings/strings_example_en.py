#This file contains some examples for Python Strings 
#What is Strings in python ?
#Strings are amongst the most popular types in Python.
#We can create them simply by enclosing characters in quotes. 
#Python treats single quotes the same as double quotes. 
#Creating strings is as simple as assigning a value to a variable.
#source of Definition https://www.tutorialspoint.com/python/python_strings.htm

#example 1
#added by @remon
str1 ="Hello World"
print(str1)

#example 2
#added by @remon
str2 ='Hello World 2'
print(str2)

#example 3
#added by @remon
str3 ="2018"
print(str3)

#example 4
#added by Salem Benlechheb
#added by @elmakikadir1983nwsn
#Now with Python you can view the number of leap
#years between two specific years. This is an example of the code you can use.
import calendar 
print(">>>>>>>>>>Leap Year Calculator<<<<<<<<<<\n")
y1=int(input("Enter the first year: ")) 
y2=int(input("Enter the second year: ")) 
leaps=calendar.leapdays(y1, y2) 
print("Number of leap years between", y1, "and", 
y2, "is:", leaps)
