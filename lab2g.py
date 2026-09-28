# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.


# Create a program calculating tax with the image above
# The script should include a variable income.
# The value of income should be a number (preferably in the thousands) inputted by the user.
# The script should also include a variable status.


# The value of status will either be "single" or "married" entered by the user.

# Use nested if, elif, and else statements to create a working model of the image above.
# Also use relational operators to compare income and status with the threshold values given in your slides.
# Test your program with multiple different numbers.

correctIncome = False
while correctIncome == False:
    income = input("\nWhat is your income? ")
    

    if income.isnumeric() == True:
        income = int(income)


        correctIncome = True
    else:
        print("You must enter a number!")


correctStatus = False
# status = input("Are you single or married?")
# status = status.lower()
while correctStatus == False:
    status = input("\nAre you single or married? ")
    status = status.lower()

    if status == "single" or status == "married" :
        correctStatus = True


    else:
        print("You must enter either \"single\" or \"married\"")

print(f"\nYour income is: {income}")
print(f"Your status is: {status}")

if status == "single":
    if income <= 32000:
        print("less or is 32000")
        tax = income * 0.10
        print(f"Your tax is: {tax}")

    elif income > 32000:
        print("more than 32000")
        tax = 3200 + ((income - 32000) * 0.25)
        print(f"Your tax is: {tax}")

elif status == "married":
    if income <= 64000:
        tax = income * 0.10
        print(f"Your tax is: {tax}")
        
    elif income > 64000:
        tax = 6400 + ((income - 64000) * 0.25)
        print(f"Your tax is: {tax}")