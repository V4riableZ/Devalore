#!/usr/bin/python

str1=raw_input("Enter a word:")
str2=raw_input("Enter another word:")

opt=[1,2,3]
num=opt

print("Choose a number: %s"%num)
num=input()

for word in str1:
    if len(str1) > len(str2):
	long_str=str1
	print(long_str)
    else:
	long_str=str2
	print(long_str)

