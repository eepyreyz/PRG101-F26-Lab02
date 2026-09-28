# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/09/28
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py

# TO DO 1: Follow the instructions given in README.md file
import sys
# - Fill in the required fields in the comment section.
# - Create a variable called name.
# - Create another variable called age.
# - The script should assign the string sys.argv[1] (first argument) to the variable "name"
# - The script should assign the string sys.argv[2] (second argument) to the variable "age".
# name = sys.argv[1]
# age = sys.argv[2]


lengOfArguments = len(sys.argv)
lengOfArgumentsRECEIVED = lengOfArguments - 1


if lengOfArguments >= 3:
    name = sys.argv[1]
    age = sys.argv[2]
    print(f"Hi {name}, you are {age} years old and the script received {lengOfArgumentsRECEIVED} arguments.")

elif lengOfArguments < 3 :
    print("The script requires at least 2 arguments.")

# - The script should use if-elif structure and should print the EXACT OUTPUT as shown below.


# **Sample Run 1:**
# ``` 
# python ./lab2f.py Maija 20 PRG101
# output: Hi Maija, you are 20 years old and the script received 3 arguments.
# ```  


# **Sample Run 2:**
# ```
# python ./lab2f.py Maija 20 PRG101 Seneca
# output: Hi Maija, you are 20 years old and the script received 4 arguments.
# ```  


# **Sample Run 3:**
# ```
# python ./lab2f.py
# output: The script requires at least 2 arguments.
# ```
