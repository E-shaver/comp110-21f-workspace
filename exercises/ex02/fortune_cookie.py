"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730396741"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint
number: int = randint(1, 3)

print("Your fortune cookie says... ")
if number == 3:
    print("You're going to find love in the near future!")
elif number == 2:
    print("Money will find you in your future.")
else:
    print("Follow your dreams and you'll find happyness.")
print("Good Luck!")
    



# Begin your solution here...