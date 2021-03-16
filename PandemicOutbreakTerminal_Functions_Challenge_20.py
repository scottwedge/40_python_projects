#!/usr/bin/env python3

# Pandemic Outbreak Terminal Application

# Get population size
# Get percentage of population to initially infect
# Get probability that a person gets infected when exposed
# Get how long the infection lasts when exposed
# Get mortality rate of the infection
# Get how long to run the simulation

# For each person status we need to track
# pop:  health (O or I or X or ???)
# days_sick:  how many days being infected
# 
# Print daily status of population (healthy, infected or dead)

# Imports
import random

# Constants
INFECTED = "I"
HEALTHY = "O"
DEAD = "X"
SPACER = "-"


# Functions
def get_pop_count():
    print("To simulate an epidemic outbreak, we must know the population size.")
    pop_count = input("--Enter the population size: ")
    pop_count = int(pop_count)  # convert from input string type to integer type
    return pop_count

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

def init_pop(pop_count, HEALTHY):
    pop = []    # initialize empty list
    for j in range(pop_count):
        pop.append(HEALTHY)
    return pop

def init_days_sick(pop_count):
    days_sick = []  # initialize empty list
    for j in range(pop_count):
        days_sick.append(0)
    return days_sick

def daily_status(pop):
    status = str(pop[0])   # first character of status
    for j in range(1, len(pop)):
        status = status + SPACER + str(pop[j])
    return status      


# Main code
# Get all inputs from user
pop_count = get_pop_count()
pop_pc = get_pop_pc()
expose_pc = get_exposure_pc()
duration = get_duration()
mort_pc = get_mort_pc()
num_days = get_num_days()

# Initialize all users to be healthy with zero days sick
pop = init_pop(pop_count, HEALTHY)
days_sick = init_days_sick(pop_count)
print("DEBUG pop=", pop)   # DEBUG
print("DEBUG days sick =", days_sick)  #DEBUG
j = input("input")

day = 1
# Calculate number of infections on day 1
infected_count = pop_count * pop_pc / 100
infected_count = int(infected_count)   # convert to integer (by rounding down)
print("DEBUG infect_counted =", infected_count)

# choose randomly who gets infected
while infected_count > 0:
    random.seed()
    infected_index = random.randint(0, pop_count - 1)  # select random person
    if pop[infected_index]  == HEALTHY:
        pop[infected_index] = INFECTED  # mark person as infected
        days_sick[infected_index] += 1
        infected_count = infected_count - 1
    else:
        print("Ignore this user since they are already =", pop[infected_index])
 
print("DEBUG pop=", pop)   # DEBUG
print("DEBUG days sick =", days_sick)  #DEBUG

status = daily_status(pop)
print("daily status: ", status)

# Now update status of everyone for day 2 until end of simulation
# use new list to avoid new updates affecting later updates
day = day + 1
new_pop = []
while day <= num_days: 
    # check status of user themself
    # if user dead then remains dead
    if pop[0] == DEAD:
        new_pop[0] = DEAD
    # if user infected, determine if dies, has recovered/healthy or is still infected
    elif pop[0] == INFECTED:
        random.seed()
        if random.randint(0,100) <= mortality_pc/duration:  # spread mortality over duration of illness (??)
            new_pop[0] = DEAD
        elif days_sick[0] >= duration:
            new_pop[0] = HEALTHY   # patient has recovered and is healthy
            new_days_sick[0] = 0
        else:                  #  days_sick[0] < duration:
            new_pop[0] = INFECTED    # still infected
            new_days_sick[0] = days_sick[0] + 1
    else:   # was HEALTHY
        if new_pop[0] != DEAD and new_pop[0] != INFECTED:
            new_pop[0] = HEALTHY    # still healthy

    # if healthy, determine if upper neighbour is infected so might infect this user
    if pop[0] == HEALTHY:   # special case for first person in row
        if pop[1] == INFECTED:    # check upper neighbour
            random.seed()
            if random.randint(0,100) <= exposure_pc:
                new_pop[0] = INFECTED
                new_days_sick = 1
            else:
                new_pop[0] = HEALTHY    # still healthy
                new_days_sick = 0

    # if healthy, determine if lower neighbour is infected so might infect this user
    if pop[0] == HEALTHY:   # special case for first person in row
        if pop[-1] == INFECTED:    # check lower neighbour
            random.seed()
            if random.randint(0,100) <= exposure_pc:
                new_pop[0] = INFECTED
                new_days_sick = 1
            else:
                new_pop[0] = HEALTHY    # still healthy
                new_days_sick = 0


    day = day + 1     
