
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/09/28
# Purpose: Practice using if, elif, and else statments.
# Usage: ./lab2c.py

# TO DO 1:
# Prmopt the user to enter a sentence, save it in the variable str1
str1 = input("Enter a sentence: ")
# Prmopt the user to enter another sentence, save it in the variable str2
str2 = input("Enter another sentence: ")
#
# Use if, elif, and else statments with the len() function to check which of the 2 is longer.
str1Length = len(str1)
str2Length = len(str2)

if str1Length > str2Length:
    print(f"{str1} is longer than {str2}")
elif str1Length < str2Length:
    print(f"{str2} is longer than {str1}")
else:
    print(f"Both {str1} and {str2} are equal in length")


# The final result should be:
# ---- is longer then ----
# If they are equal then print:
# ---- and ---- are equal.
# Get input from the user



