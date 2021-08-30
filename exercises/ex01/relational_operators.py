"""Relational operator demonstration"""
__author__ = "730396741"

x: str = input("Left-hand side: ")
y: str = input("Right-hand side: ")
number = (int(x) < int(y))
print(str(x) + " < " + str(y) + " is " + str(number))
number = (int(x) >= int(y))
print(str(x) + " >= " + str(y) + " is " + str(number))
number = (int(x) == int(y))
print(str(x) + " == " + str(y) + " is " + str(number))
number = (int(x) != int(y))
print(str(x) + " != " + str(y) + " is " + str(number))