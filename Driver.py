#!/usr/bin/env python3
#programed by Jason Renna
from MoveWithPercision2 import *
var = ""
while var != "exit":
   var = input("Please enter something: ")
   if var == "forward":
       #moveStraightWithPercision()
       move_foward()
       print("forward")
   elif var == "left":
       turnLeftWithPercision()
       print("left")
   elif var == "right":
       turnRightWithPercision()
       print("right")
   elif var == "exit":
       print("closing program")
   else:
       print("invalid input")
