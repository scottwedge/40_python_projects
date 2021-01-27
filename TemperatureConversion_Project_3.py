#!/usr/bin/env python3

# Script to convert temperature from Fahrenheit to Celcius and Kelvin
# Results to be accurate to four decimal places and aligned in a table

# Functions
def f_to_c(f_num):
    c_temp = (f_num - 32) * 5 / 9
    return c_temp

def c_to_k(c_temp):
    k_temp = c_temp + 273.15
    return k_temp

def main():
    # Print welcome and purpose of application
    print("Welcome to the temperature conversion application.")
    
    # Get user (string) value in Fahrenheit
    user_temp = input("Please enter the temperature in Fahrenheit: ")
    
    # Convert user input string value to float type
    f_temp = float(user_temp)
    
    # Convert temperature to Celcius
    c_temp = f_to_c(f_temp)
    
    # Convert temperature to Kelvin
    k_temp = c_to_k(c_temp) 
    
    # Display both conversion values with results accurate to four decimal places.
    # formatting syntax is left align with two decimal places is '{:<11.2f}'
    # center aligned with four decimal places is '{:^14.4f}'
    # right aligned with four decimal places is '{:>18.4f}'
    # seems that we need to use left alignment according to video demonstration with F > 250
    print("Degrees Fahrenheit:     {:<8}".format(f_temp))
    print("Degrees Celsius:        {:<8.4f}".format(c_temp))
    print("Degrees Kelvin:         {:<8.4f}".format(k_temp))
    
if __name__ == '__main__':
    main()
