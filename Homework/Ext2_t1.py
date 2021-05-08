#!/usr/bin/python

from __future__ import division
import os

os.system('clear')

num1=int(input('Please enter a number:'))
num2=int(input('Please enter another number:'))

numSum=num1+num2
numMulti=num1*num2
numDiv=num1/num2

print("The summary of the numbers is: %s"%numSum)
print("The numbers are multiplied and the result is: %s"%numMulti)
print("The numbers are then divided and the result is: %s"%numDiv)

if num1 == num2:
	print("The numbers are equal: %s"%num1,num2)
else:
	print("The numbers are unequal: %s"%num1,num2)

if num1 > num2:
	print("The first number is bigger than the second number, %s"%num2)
else:
	print("The second number is bigger than the first number, %s"%num1)
