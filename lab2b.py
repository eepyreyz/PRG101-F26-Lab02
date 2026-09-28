# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date:2026/09/28
# Purpose: Practice using if and else statments.
# Usage: ./lab2b.py



# - Fill in the required fields in the comment section.
# - Use the input() function and ask the user to enter a 4 digit integer. Save this value in the variable `num`.
num = input("Enter a 4 digit integer: ")
num = int(num)
# - The program should print out "George Orwell" if the number is exactly 1984, and otherwise prints “Not quite right!”. Use `if`, and `else` statement.
if num == 1984:
    print("George Orwell")
else:
    print("Not quite right!")