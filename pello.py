#!/usr/bin/env python3

import os
import time
import getpass
import sys
from pwd import getpwnam

def getuser():  #Gets user name and uid

    topuser = 0
    User = ""
    User = getpass.getuser()
    Userid  = getpwnam(User).pw_uid

    if Userid == topuser:
        print ("Root is not allowed to run this script")

    else:
       print('Hello' , User)
       #print(user)



sec = 3

getuser()
time.sleep(sec)
os.system('clear')
