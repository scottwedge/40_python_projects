#!/usr/bin/env python3

# Pandemic Outbreak Terminal Application

# Get population size
# Get percentage of population to initially infect
# Get probability that a person gets infected when exposed
# Get how long the infection lasts when exposed
# Get mortality rate of the infection
# Get how long to run the simulation

# Imports
import random


# Functions
def get_pop():
    print("To simulate an epidemic outbreak, we must know the population size.")
    pop = input("--Enter the population size: ")
    pop = int(pop)  # convert from input string type to integer type
    return pop

def get_pop_pc():
    print()   # blank line
    print("We must first state by infecting a portion of the population.")
    pop_pc = input("--Enter the percentage (0-100) of the population to initially infect: ")
    pop_pc = float(pop_pc)/100  # convert to integer type
    return pop_pc

def get_exposure_pc():
    print()   # blank line
    print("We must know the risk a person has to contract the disease when exposed.")
    exposure_pc = input("--Enter the probability (0-100) that a person gets infected when exposed:  ")
    exposure_pc = float(exposure_pc)/100  # convert to integer type
    return exposure_pc

def get_duration():
    print()   # blank line
    print("We must know how long the infection will last when exposed.")
    duration = input("--Enter the duration (in days) of the infection: ")
    duration = int(duration)
    return duration

def get_mort_pc():
    print()   # blank line
    print("We must know the mortality rate of those infected.")
    mort_pc = input("--Enter the mortality rate (0-100) of the infection: ")
    mort_pc = float(mort_pc)/100
    return mort_pc

def get_num_days():
    print()  # blank line
    print("We must know how long to run the simulation.")
    num_days = input("--Enterthe number of days to simulate: ")
    num_days = int(num_days)  # convert to integer type



# Main code
pop = get_pop()
pop_pc = get_pop_pc()
expose_pc = get_exposure_pc()
duration = get_duration()
mort_pc = get_mort_pc()
num_days = get_num_days()
