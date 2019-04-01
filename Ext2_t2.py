#!/usr/bin/env python3

import os
os.system('clear')

str1=input("Enter a word:")
str2=input("Enter another word:")

num=int(input(("Choose a number: [1,2,3] ")))

if len(str1) > len(str2):
    print("Longest word '%s'"%str1)

elif len(str1) < len(str2):
    print("Longest word '%s'"%str2)

else:
	print("Words are equal in length")

if str1 in str2:
	print("The first word contains a string from the second word!")
else:
	print("Words are different in letters")




