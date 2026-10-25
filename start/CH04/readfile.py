#!/usr/bin/env python3
# Sample script that reads a file
# By  August martin

print ('Heres someone to hack: ')
Hackme= open("Hackme.txt", 'r')

Details = Hackme.read()
print (Details)

Hackme.close()