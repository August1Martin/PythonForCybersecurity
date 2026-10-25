#!/usr/bin/env python3
# Sample script that writes to a file
# By  August martin


f = open('Hackme.txt', 'w')
names = input('What is ur first and Last name? ')
color = input('Whats is your favorite color? ')
Pets = input('Whats your pets first name? ')
Mother = input('What is your mothers maiden name? ')
elementary = input('What elementary school did you attend? ')
f.write ('\nI see ur name is ' + names)
f.write ('\nI See ur favorite color is' + color)
f.write ('\nAnd i know ur pets Name is ' + Pets)
f.write ("\nalso ur mothers maiden name " + Mother)
f.write ("\nAnd I know u went to " + elementary)

f.close()