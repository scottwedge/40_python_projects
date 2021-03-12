#!/usr/bin/env python3

# Pandemic Outbreak Terminal Application

# Get population size
# Get percentage of population to initially infect
# Get probability that a person gets infected when exposed
# Get how long the infection lasts when exposed
# Get mortality rate of the infection
# Get how long to run the simulation

# For each person status we need to track
# index 0: (health_index) health (O or I or X or ???)
# index 1: (days_infected_index) if infected, how many days being infected
# index 2: TBD ???

# Imports
import random

# Constants
INFECTED = "I"
HEALTHY = "O"
DEAD = "X"
SPACER = "-"
STATUS_SIZE = 2 # number of status entries for each person
HEALTH_INDEX = 0
DAYS_INFECTED_INDEX = 1



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
    pop_pc = int(pop_pc)  # convert to integer type
    return pop_pc

def get_exposure_pc():
    print()   # blank line
    print("We must know the risk a person has to contract the disease when exposed.")
    exposure_pc = input("--Enter the probability (0-100) that a person gets infected when exposed:  ")
    exposure_pc = int(exposure_pc)  # convert to integer type
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
    mort_pc = int(mort_pc)
    return mort_pc

def get_num_days():
    print()  # blank line
    print("We must know how long to run the simulation.")
    num_days = input("--Enter the number of days to simulate: ")
    num_days = int(num_days)  # convert to integer type

def init_config(pop, STATUS_SIZE):
    pop_status = []
    default_state = [HEALTHY, 0]
    for j in range(pop):
        pop_status.append(default_state)
    return pop_status


# Main code
# Get all inputs from user
pop = get_pop()
pop_pc = get_pop_pc()
expose_pc = get_exposure_pc()
duration = get_duration()
mort_pc = get_mort_pc()
num_days = get_num_days()

# Initialize all users to be healthy 
pop_status = init_config(pop, STATUS_SIZE)

day = 1
# Initial infection count
infect_count = pop * pop_pc / 100
infect_count = int(infect_count)   # convert to integer (by rounding down)
for k in range(infect_count):
    # create list of all healthy population
    healthy_list = []
    for j in range(pop): # evaluate every user
        if pop[j][HEALTH_INDEX] == HEALTHY:
            healthy_list.append(j)
        healthy_list.append   # create list of healthy pop
                              # randomly infect from healthy pop list
    infected_index = random.randint(1, len(healthy_list))
    pop[infected_index][HEALTH_INDEX] = INFECTED
print(pop)    
    

#while day <= num_days:
    
# Daily status updates
# 
