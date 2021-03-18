#!/usr/bin/env python3

# Fooling around with local and global variables

x = "awesome"

def myfunc():
    global x
    x = "Terrific"

myfunc()

print("Python is " + x)
