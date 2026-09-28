# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/09/28
# Purpose: Learn how to use while loops for validating user input.
# Usage: ./lab2i.py

# TO DO 1: 
# Creat variable pin. The value of pin should be a 4 digit code inputted by the user.
# Add a while loop to create program that wont end until the user enters 1234.

correctPinNum = 1234
opened = False
while opened == False:
    pin = input("Please type in your PIN: ")

    if pin.isnumeric() == True: #Check if its numbers

        pin = int(pin) #Now convert

        if pin != correctPinNum: #Wrong pin
            print("Incorrect...try again")

        elif pin == correctPinNum: #Right pin
            print("Correct PIN, You can enter!")
            opened = True

    else: #Not numbers, error, and try again
        print("The PIN must be a number")




# Follow the specific instructions given in the README.md file.

#guess = 5
#number = int(input("Guess what number less than 10 I am thinking off?"))
#while number != guess:  # loop condition 
#  print("incorrect guess, try again...")
# number = int(input("Guess what number less than 10 I am thinking off?")) # keep taking input from user until the user enters the correct guess.
#print("You got it right!") # this statement will be executed when loop has terminated which will only happen when the user enters the number 5.
# Define the correct PIN
