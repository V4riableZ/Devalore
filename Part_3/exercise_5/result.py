#Class which reads file data to a variable and prints the variable.
#Imported OS library for specific directory usage

import os 
file = open(os.path.expanduser('~/Desktop/py3/Part_3/exercise_5/s.txt') , "r").read()
print(file)
