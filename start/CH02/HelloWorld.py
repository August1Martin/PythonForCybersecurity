#!/usr/bin/env python3
# A simple "Hello World" script in python
# Created by August Martin Sep 29 2026





#Get user name
user_name = input('What is your name? ')
#print hello +user name
message=('hello '+ user_name)
message1=(' I hope u have a great day!')
print (message + message1)
#gets the users age
user_age= input('How old are u ')
#the number it calls to add 
my_number= 2
#converts the users name to a int so my number can be added when new age is call upon
new_age= int(user_age) + my_number 
#converts new age to a str so it can be added to the message
message3= ('In 2 years, you will be ' + str(new_age) + ' years old')
print (message3)