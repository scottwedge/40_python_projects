#!/usr/bin/env python3

# Welcome banner
# Explain format of a quadratic equation 
# Ask how many equations will be solved today.


print("Welcome to the Quadratic Solver App.")
print() # blank line

print("A quadratic equation is of the form ax**2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")

print()
num_eq = input("How many equations would you like to solve today: ")
num_eq = int(num_eq) # convert string input to integer

for j in range(1, num_eq + 1):
    print() # blank line
    print("Solving equation #{}".format(j))
    print("----------------------------------------------------")
    print() # blank line
    a = input("Please enter your value of a (coefficient of x**2): ")
    b = input("Please enter your value of b (coefficient of x): ")
    c = input("Please enter your value of c (coefficient): ")
    print() # blank line
    print("Your solutions to {}x**2 + {}x + {} are:".format(a, b, c))

