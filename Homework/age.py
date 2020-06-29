#!/usr/bin/python3

from multiprocessing import Process
p = Process(target=tomonths)
p.start()
p2 = Process(target=toyears)
p2.start()
p.join()
p2.join()

def tomonths():
    months = 12
    age1=int(input('Enter your age '))
    ageM=int(age1) * int(months)
    print('Your age in months is' ,ageM)

#tomonths()

def toyears():
    years = 12
    age2=int(input('Enter your age in months '))
    ageY=int(age2) / int(years)
    print(('Your age in months is ',abs(ageY))

#toyears()
