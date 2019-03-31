#!/usr/bin/env bash
script_name=''

echo "Script will be made with .py ending!!"

echo "Enter python3 script name"
read script_name

if [ -e $script_name  ]; then
		echo "File $script_name already exists!"
		else
  			touch "$script_name.py"
			echo "#!/usr/bin/env python3" >> $script_name

fi



