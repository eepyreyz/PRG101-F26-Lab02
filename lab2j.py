# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/09/27
# Purpose: Learn how to use while loops with break and continue.
# Usage: ./lab2j.py

# TO DO 1: 
# Import the `math` module.
import math
# Define a variable named num. Prompt the user to input a number and assign it to the variable num.
# Convert the user input to a floating-point number and assign it to num.


# TO DO 2: 
# Create an infinite loop using while True. Inside the loop:
while True:
    num = input("Please type in a number: ")
    num = float(num)
# Check if num is negative:
    if num < 0:                 
        print("Invalid number.") # If it is, print "Invalid number." and continue to the next iteration of the loop.
        continue

# TO DO 3: 
    elif num == 0: # Check if num is zero:
        print("Exiting...")
        break # If it is, print "Exiting..." and break out of the loop.

    else:
        num = math.sqrt(num)
        print(num)


