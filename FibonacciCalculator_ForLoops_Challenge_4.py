#!/usr/bin/env python3

# Print welcome header.
# Calculate the first n terms of the Fibonacci sequence.
# Then calculate the ratio of consecutive Fibonacci numbers.
# Which should approach 1.618

# Functions
def header():
    print("Welcome to the Fibonacci Calculator App.")
    print() # blank line

def fib(last, second_last):
    return last + second_last

def get_num():
    num = input("How many digits of the Fibonacci Sequence would you like to compute: ")
    num = int(num) # convert input string to integer
    print() # blank line
    return num

def create_fib_list(num):
    fib_list = [1, 1] # most common case
    if num == 1:
        fib_list = [1]
    elif num >= 2:
        for j in range(3, num+1):
            fib_list.append(fib(fib_list[-1], fib_list[-2]))
    else:
        fib_list=[]
    return fib_list

def main():
    header()    
 
    num = get_num()
 
    
    # Create list of first num Fibonacci sequence, then display it.
    fib_list = create_fib_list(num)
    if fib_list == []:
        print("number must be integer greater than zero")
    else:
        print("The first {} numbers of the Fibonacci sequence are: ".format(num))
        for j in range(num): 
            print(fib_list[j])  # print Fibonacci number from list
    
    print() # blank line
    print("The corresponding Golden Ratios are: ")
    # Calculate Golden Ratio (last number divided by second last number) and print
    for j in range(2, num+1):
        gr = fib_list[j-1]/fib_list[j-2]
        print(gr)
    
    print() # blank line
    print("The ratio of consecutive Fibonacci terms approaches Phi: 1.618...")
    
if __name__ == "__main__":
    main()
