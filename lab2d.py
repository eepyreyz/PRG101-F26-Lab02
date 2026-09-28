# python3 lab2d.py

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: Learn how to use command line arguments.
# Purpose: .
# Usage: ./lab2d.py
import sys
print(sys.argv)
# TO DO 1: copy the required lines from README.md to print version, platform, argv and the length of argv.

# run the script in the terminal using command: python ./lab2d.py

print(sys.version) # prints the version of the python currently in use.
print(sys.platform) # prints the name of operating system.
print(sys.argv) # prints the list of all arguments given at the command line when running our python script from terminal.
print(len(sys.argv)) # tells us the number of command line arguments the user provides from terminal.


print("-" * 15)
# TO DO 2: copy the required lines from README.md to print argv[0], argv[1] and argv[2]print(sys.argv[0]) # prints the first argument, it is always the name of script.
print(sys.argv[1]) # prints the second argument .
print(sys.argv[2]) # prints the third argument.
print(len(sys.argv)) # tells us the number of command line arguments the user provides from terminal.

# run the script using the following command: python lab2d.py maija Maija

# - What do you observe? What did you learn?  This time we provided three arguments.
# The name of script is the first argument, second argument is maija and third argument is Maija.
"""
I learned that we can run python lab2d.py followd by anything, and it will act as an input/arguments and save in sys.argv.
I also learned that it saves it in sys.argv a list, the first element with index 0 is always the file name.
When I ran the command python lab2d.py maija Maija, i noticed that my arguments saved in a list in sys.argv where the 
first element was lab2d.py (index 0), second element was maija (index 1), and third element was Maija(index3).

The main diffrence between input() and using the command line is,
When input is used it asks for the input after the script starts, but when we use the command lines we have to type our arguments
when we run the script.

sys.version shows the python version currently used
sys.platform names the operating system
You can use len(sys.argv) to figure out hwo many arguments u have in sys.argv including the file name.
"""