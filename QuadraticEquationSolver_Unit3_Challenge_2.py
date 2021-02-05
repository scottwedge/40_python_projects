#!/usr/bin/env python3

# Welcome banner
# Explain format of a quadratic equation 
# Ask how many equations will be solved today.

import cmath

def main():
    print("Welcome to the Quadratic Solver App.")
    print() # blank line
    
    print("A quadratic equation is of the form ax**2 + bx + c = 0")
    print("Your solutions can be real or complex numbers.")
    print("A complex number has two parts: a + bj")
    print("Where a is the real portion and bj is the imaginary portion.")
    
    print()
    num_eq = input("How many equations would you like to solve today: ")
    num_eq = int(num_eq) # convert string input to integer
    
    for n in range(1, num_eq + 1):
        print() # blank line
        print("Solving equation #{}".format(n))
        print("----------------------------------------------------")
        print() # blank line
        a = input("Please enter your value of a (coefficient of x**2): ")
        a = float(a)
        b = input("Please enter your value of b (coefficient of x): ")
        b = float(b)
        c = input("Please enter your value of c (coefficient): ")
        c = float(c)
        print() # blank line
        print("Your solutions to {}x**2 + {}x + {} are:".format(a, b, c))
    
        # d = b**2 - 4*a*c
        # sol1 =  (-b-cmath.sqrt(d))/(2 * a)
        # sol1 =  (-b+cmath.sqrt(d))/(2 * a)
    
        d = b**2 - 4*a*c
        sol1 =  (-b-cmath.sqrt(d))/(2 * a)
        sol2 =  (-b+cmath.sqrt(d))/(2 * a)
    
        print("        x1 is: {}".format(sol1))
        print("        x2 is: {}".format(sol2))
        
    print() # blank line
    print("Thank you for using the Quadratic Solver App. Goodbye.")

if __name__ == "__main__":
    main()
