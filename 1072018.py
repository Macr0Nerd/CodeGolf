"""
Challenge for the week of 10/07/2018
------------------------------------
This is our first challenge so we are going to start off sort of easy.
This week's challenge is to take a string input and output the string mockingly.

For instance:
"hello world" ---> "HeLlO WoRlD"
"stop mocking me" ---> "StOp mOcKiNg mE"

In order to be considered a valid solution, the capitalization of characters must be alternating.
You may assume the starting string is all lower case
You do not need to define a function with inputs and outputs, accept user input, or hard code a string.
The existence of the string is implied and adding these things in increases character count to an extreme degree in some languages (looking at you, Java).
"""

x="stop mocking me" #not counted
y=list(x);y[::2]=x[::2].upper()
print(''.join(y)) #not counted