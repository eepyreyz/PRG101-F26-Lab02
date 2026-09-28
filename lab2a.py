# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/09/28
# Purpose: Create a variable, check its type and print the variable.
# Usage: ./lab2a.py

# - Fill in the required fields in the comment section.
# - Create a variable x, and set its value as a number inputted from the user. 
x = input("Enter a number: ")

# - Use the `type()` function to check the type of `x`.
print(type(x))
# - You will notice that the type of `x` is `str`.
# - Convert `x` to integer.
x = int(x)
# - Write an if-statement to evaluate the expression if x is greater than or equal to 6.
if x >= 6:
# - If the expressions evaluates to TRUE, print: `"x is greater then 6!"
    print(f'{x} is greater than 6!')
# - Next write another if statement combining both relational and Boolean operator to evaluate the expression 
# if x is greater than or equal to 4 and x is less than 12.

if x >= 4 and x < 12:
    print(f'{x} is equal to 4 or greater than 4 and less than 12 ')
# - Print the appropriate message to user if the expression evaluates to TRUE