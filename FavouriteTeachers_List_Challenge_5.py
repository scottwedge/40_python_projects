#!/usr/bin/env python3

# Favourite teachers program

# Welcome user to Favourite Teachers Program
# Create list by prompting for teachers' first names in any format.
# Then list teachers in order entered in title format
# Then list teachers alphabetically
# Then list them in reverse alphabetical order.
# Then list top two teachers.
# Then list the next two favourites.
# Then list the last favourite.
# Then list the total number.
# Then warn that first is no longer your favourite and prompt for new FAVOUITE
# Then list all teachers in favourite, alphabetical and reverse alphabetical orders and total number of teachers
# Then prompt to remove one teacher and relist allo

 
print("Welcome to the Favourite Teachers Program")
print() # blank line

# get first four favourite teachers
teacher_list = [] # initialize blank list
count_list = ["first", "second", "third", "fourth"]
for j in count_list:
    teacher_input = input("Who is your {} favourite teacher: ".format(j))
    
    teacher = teacher_input.title() # convert to title format
    teacher_list.append(teacher)
    teacher_alpha = teacher_list.copy()
    teacher_alpha.sort() # sort alphabetically
    teacher_revalpha = teacher_alpha.copy()
    teacher_revalpha.reverse() # sort reverse alphabetically
    
# Display teachers in different orders
print() # blank line
print("Your favourite teachers ranked are:", teacher_list)  # list in order of entry
print("Your favourite teachers alphabetically are: {}". format(teacher_alpha))
print("Your favourite teachers in reverse alphabetical order are: {}".format(teacher_revalpha))


