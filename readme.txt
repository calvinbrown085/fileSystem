Readme for file
Authors: Calvin Brown, Chad Gilmer

Files:
reader.py
Utilities.py

Reader.py:
this is the file to run, it contains the shell that we are using to open the file being passed in and that is also where it takes the commands from the userInput
Use Cases:
Stat <filename>, gives information on the file <filename>
info, this will use whatever file you passed in when running the file
ls, this will list all directories in the file you passed in
cd <location>, will change the location to <location>

Utilities.py
Nothing really useful, most of these functions just get used in the Reader.py file.
This file is just for clean code and fucntionnes to keep our functions clean and code easy to read.


How To Run?
go into the fileSystem directory and run
"python3 reader.py <filename>"
use filename of whatever you would like to pass into the file.
