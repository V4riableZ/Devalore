#!/usr/bin/env bash
clear
echo "Script will be created with .py ending!!"

read -p "Please enter script name: " filename
if [ -e "$filename.py" ]; then
       echo "File Already exists!"
       exit
else
touch $filename.py
chmod +x $filename.py
echo "#!/usr/bin/env python3" >> "$filename.py"
read -p "Do you want to open the file now? Y/N " answer
fi
if [ $answer == y ] || [ $answer == Y ]; then
       nano "$filename.py"
else
       exit
fi

#Script by or bracha


