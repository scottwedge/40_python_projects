#!/usr/bin/env python3

# Project 4 involves right angle triangle
# Need to calculate hypotenuse and area of triangle.

# Welcome user, then prompt for length of two sides.
# Then display hypotenuse and area accurate to three decimal spaces.

# Functions
def calc_hyp(a, b):
    hyp = (a**2 + b**2) ** 0.5
    return hyp

def calc_area(a, b):
    area = 0.5 * a * b
    return area

# Welcome user and state purpose of application.
print("Welcome to the right angle triangle application")

# Prompt for first side length.
user_side_1 = input("What is the first leg of the triangle: ")
side1 = float(user_side_1)

# Prompt for second side length.
user_side_2 = input("What is the second leg of the triangle: ")
side2 = float(user_side_2)

# Calculate hypotenuse (square root of sum of square of other two sides)
hypotenuse = calc_hyp(side1, side2)

# Display length of hypotenuse accurate to three decimal places.
print("For a triangle with legs of {} and {} the hypotenuse is {:.3f}.".format(side1, side2, hypotenuse))

# Calculate area of triangle (half of one side multiply by other side)
area = calc_area(side1, side2)

# Display area of triangle accurate to three decimal places.
print("For a triangle with legs of {} and {} the area is {:.3f}.".format(side1, side2, area))

