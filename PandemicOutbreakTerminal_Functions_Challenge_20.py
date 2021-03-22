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
    print("We must first start by infecting a portion of the population.")
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
    return num_days

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

def format_daily_status(pop):
    status = str(pop[0])   # first character of status
    for j in range(1, len(pop)):
        status = status + SPACER + str(pop[j])
    return status      

def update_user(pop, new_pop, days_sick, new_days_sick, mort_pc, duration):
    for j in range(len(pop)):
        # check status of user themself
        if pop[j] == DEAD:    # if user was dead then remains dead
            new_pop[j] = DEAD
        elif pop[j] == INFECTED:   # if user was infected, determine if dies, has recovered/healthy or is still infected
            random.seed()
            if random.randint(0,100) <= mort_pc/duration:  # spread mortality over duration of illness (??)
                new_pop[j] = DEAD
                new_days_sick[j] = 0
            elif days_sick[j] >= duration:
                new_pop[j] = HEALTHY   # patient has recovered and is healthy
                new_days_sick[j] = 0
            else:                  #  days_sick < duration:
                new_pop[j] = INFECTED    # still infected
                new_days_sick[j] = days_sick[j] + 1
        else:   # was HEALTHY
            new_pop[j] = pop[j]    # still healthy
    return (new_pop, new_days_sick)

def check_neighbour(pop, new_pop, days_sick, new_days_sick, offset, expose_pc):
# if offset = -1 then check if lower neighbour infected
# if offset = 1 then check if upper neighbour infected
    for j in range(len(pop)):
        if (j == 0 and offset == -1) or (j == len(pop) - 1 and offset == 1): # special end cases
            continue
        else: 
            if pop[j] == HEALTHY and new_pop[j] == HEALTHY:         # if user now and next day is healthy
                if pop[j + offset] == INFECTED:    # check neighbour
                    random.seed()
                    if random.randint(0,100) <= expose_pc:
                        new_pop[j] = INFECTED
                        new_days_sick[j] = 1
                    else:
                        new_pop[j] = HEALTHY    # still healthy
                        new_days_sick[j] = 0
    return (new_pop, new_days_sick)

def summary(new_pop, day):
    status = format_daily_status(new_pop)
    infect = 0
    dead = 0
    total = len(new_pop)
    for j in new_pop:
        if j == DEAD:
            dead = dead + 1
        elif j == INFECTED:
            infect = infect + 1

    infect_pc = 100 * infect / total
    dead_pc = 100 * dead / total        
 
    print() # blank line
    print("-----Day # {} -----".format(day))
    print("Percentage of Population Infected: {}%".format(infect_pc))
    print("Percentage of Population Dead: {}%".format(dead_pc))
    print("Total People Infected: {} / {}".format(infect, total))
    print("Total Deaths: {} / {}".format(dead, total))

# Main code
def main():
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
    
    day = 1
    # Calculate number of infections on day 1
    infected_count = pop_count * pop_pc / 100
    infected_count = int(infected_count)   # convert to integer (by rounding down)
    
    # choose randomly who gets infected
    while infected_count > 0:
        random.seed()
        infected_index = random.randint(0, pop_count - 1)  # select random person
        if pop[infected_index]  == HEALTHY:
            pop[infected_index] = INFECTED  # mark person as infected
            days_sick[infected_index] += 1
            infected_count = infected_count - 1
        else:
            pass
    
    summary(pop, day)
    status = format_daily_status(pop)
    print(status)   # print day #1 health status
    j = input("Press enter to begin the simulation.")
    loop_forever = True
    
    while loop_forever: 
        day = day + 1
        status = format_daily_status(pop)
    
        new_pop = init_pop(pop_count, HEALTHY)     # set all of next day's status to HEALTHY by default
        new_days_sick = init_days_sick(pop_count)   # set all of next day's sick day count to zero
    
        (new_pop, new_days_sick) = update_user(pop, new_pop, days_sick, new_days_sick, mort_pc, duration)   # update user based on previous health setting
    
        # if user healthy, determine if lower neighbour is infected so might infect this user
        offset = -1    # check lower neighbour
        (new_pop, new_days_sick) = check_neighbour(pop, new_pop, days_sick, new_days_sick, offset, expose_pc)
    
        # if user healthy, determine if upper neighbour is infected so might infect this user
        offset = 1    # check upper neighbour
        (new_pop, new_days_sick) = check_neighbour(pop, new_pop, days_sick, new_days_sick, offset, expose_pc)
        
        summary(new_pop, day)
        print(status)
      
        if day < num_days:
            j = input("Press enter to advance to the next day.")
        else:
            loop_forever = False  # exit loop since simulation over
    
    
        pop = new_pop.copy()  # overwrite old health status results with latest results
        days_sick = new_days_sick.copy()  # overwrite old sick days count with latest values

if __name__ == "__main__":
    main()
