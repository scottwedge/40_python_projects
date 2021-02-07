#!/usr/bin/env python3

# Print welcome header.
# Calculate the first n terms of the Fibonacci sequence.
# Then calculate the ratio of consecutive Fibonacci numbers.
# Which should approach 1.618

# Functions
def fib(last, second_last):
    return last + second_last

print("Welcome to the Fibonacci Calculator App.")
print() # blank line

num = input("How many digits of the Fibonacci Sequence would you like to compute: ")
num = int(num) # convert input string to integer
print() # blank line

print("The first {} numbers of the Fibonacci sequence are: ".format(num))

# Create list of first num Fibonacci sequence, then display it.
fib_list = [1, 1] # most common case
if num == 1:
    fib_list = [1]
elif num >= 2:
    for j in range(3, num+1):
        fib_list.append(fib(fib_list[-1], fib_list[-2]))
else:
    print("number must be integer greater than zero")

print(fib_list)

