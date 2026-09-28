# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/09/27
# Purpose: use for loop.
# Usage: ./lab2k.py

# Write a Python program that calculates the sum of all even numbers from 1 to 100 (inclusive).
# Use a for loop to iterate over the range of numbers from 1 to 100.
# Inside the loop, check if the current number is even.
# If the number is even, add it to a running total.
# After the loop, print the final sum.

total = 0
for num in range (1,101):
    if num % 2 == 0:

        total = total + num

print(f"final sum {total}")


# The readme is so diffrent, i followed the read me

# TO DO 1: 
#Follow the instructions given in the README.md file.
# fruits = ["apple", "banana", "cherry", "date"]
# Use a for loop to iterate over the list
# for fruit in fruits:
#     print(fruit)

#for loop is commonly used with range functions. Here's another example using the range function to print numbers from 0  to 5.
