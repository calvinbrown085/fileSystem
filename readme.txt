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
You should only run this file when running the program

Utilities.py
Nothing really useful, most of these functions just get used in the Reader.py file.
This file is just for clean code and fucntionnes to keep our functions clean and code easy to read.

read.py:
This file executes the read portion of the project, it is used in the Reader.py file, nothing in this file should be called directly

info.py:
This file gives info on the boot sector of the file system that you passed in, again this file is used in the the reader.py for the info function

lsinfo.py:
This file exectues the ls portion of the project, it is called from the Reader.py when you type ls

statInfo.py:
This file executes the stat portion of the project, it is called from Reader.py when you call it with a file

changeDirectory.py:
This file will change the directory that you are in, it will check to make sure that the place you want to go is actually a directory,*Note:
There is a small problem with this, you aren't able to navigate up directories once you go down.




How To Run?
go into the fileSystem directory and run
"python3 reader.py <filename>" when testing I used the fat32.img file so that would replace the filename.
use filename of whatever image or fat32 filesystem you would like to pass into the file.
