#!/usr/bin/env python3

opt=[1,2,3]

str1=input("Enter a word:")
str2=input("Enter another word:")

num=int(input(("Choose a number: %s "%opt)))

if len(str1) > len(str2):
    print(str1)
else:
    print("Longest word %s"%str2)

