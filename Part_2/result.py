import os
from pathlib import Path
import glob 

#Define path to lookup folders and files
home_path = os.path.expanduser('~/Desktop/py3/Part_2/main_folder/')

#Print all the pictures located at path 
print("\nPicture locations")
result = list(Path(home_path).glob('**/*.jpg'))
print("\n".join(map(str, result)))

#Print all the picture files located at path 
print("\nPicture files")
print("\n".join(list(map(os.path.basename, result))))

#Print all the pictures , numbered ,  at path 
print("\nPicture files by number")
print("\n".join(map(lambda x: "%s. %s" % x, enumerate(result))))

#Print lenth of folder list
print("\nNumber of folders")
resultfolders = list(Path(home_path).glob('**'))
print(len(resultfolders))

#Print ALL folders numbered
print("\nFolders numbered")
resultfolders = list(Path(home_path).glob('**'))
print("\n".join(map(lambda x: "%s. %s" % x, enumerate(resultfolders))))

#Attempt to create dictionary of images found at path by their parent folders
print("\nPictures by folder")
entries = (map(lambda folder_name: (folder_name, (os.listdir(home_path))), result))   
print("".join(str(dict(entries))))

#Print folders containing character 'i' 
print("\nFolders containing character 'i'")
dirs = (list(Path(home_path).glob('**/*i*/**')))
print("\n".join(map(lambda x: "%s. %s" % x, enumerate(dirs))))