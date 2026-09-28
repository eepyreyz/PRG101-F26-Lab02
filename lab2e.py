# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2028/09/28
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

# TO DO 1: Follow the instructions given in README.md file


### lab2e.py
# - Fill in the required fields in the comment section.
# - Copy the contents of lab2d.py into lab2e.py file.
import sys



# - Remove the unnecessary lines which print version, platform and list of arguments.
# - For this script, we are interested in how many arguments are provided after the script name. This is important because your script needs the arguments to receive data from user.
# - Let’s assume that our script requires exactly two arguments.

# - Modify the script, use an if-elif statement to check how many arguments are passed.
# - The script should print a message if zero arguments were passed, or if not exactly 2 arguments are provided when running the script. The script should print the EXACT OUTPUT as shown.



#   **Sample Run 1:**
#   ```
#   python ./lab2e.py
#   output: This script requires exactly two arguments. No arguments were provided!
#   ```
if len(sys.argv) == 1:
    print("This script requires exactly two arguments. No arguments were provided!")

#   **Sample Run 2:**
#   ```
#    python  ./lab2e.py maija Maija
#    output: Hello user, good job, your provided two arguments!
#   ```
elif len(sys.argv) == 3:
    print("Hello user, good job, your provided two arguments!")


#    **Sample Run 3:**
#   ```
#   python ./lab2e.py 1 2 3
#   output: This script requires exactly two arguments. You provided three arguments.
#   ```
elif len(sys.argv) == 4:
    print("This script requires exactly two arguments. You provided three arguments.")
