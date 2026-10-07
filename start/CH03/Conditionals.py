#!/usr/bin/env python3
# example workign with conditionals
#By August Martin 10/7/2026


today = input('Is today a good day? (y/n) ')
print (today)
if (today == 'y' or today == 'Yes' or today == "yes" or today == 'Y'):
     for x in range (10):
            print  ("Yes it is")
    
elif (today == 'N' or today == 'no' or today == 'No' or today == "n"):      
    print ('I hope yours gets better')

else: print ('Wrong input')


