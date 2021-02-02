#!/usr/bin/env python3

# Favourite teachers program

# Welcome user to Favourite Teachers Program
# Create list by prompting for teachers' first names in any format.
# (Convert and store names in title format)
# Then list teachers in order entered in title format
# Then list teachers alphabetically
# Then list them in reverse alphabetical order.
# Then list top two teachers.
# Then list the next two favourites.
# Then list the last favourite.
# Then list the total number.
# Then warn that first is no longer your favourite and prompt for new FAVORITE
# Then list all teachers in favourite, alphabetical and reverse alphabetical orders and total number of teachers
# Then prompt to remove one teacher and relist all


# Functions
def get_names():
    teacher_list = [] # initialize blank list
    count_list = ["first", "second", "third", "fourth"]
    for j in count_list:
        teacher_input = input("Who is your {} favourite teacher: ".format(j))
        teacher = teacher_input.title() # convert names to title format
        teacher_list.append(teacher)
    return teacher_list

def sort_alpha(teacher_list):
    teacher_alpha_list = teacher_list.copy()
    teacher_alpha_list.sort() # sort alphabetically
    return teacher_alpha_list

def sort_rev_alpha(teacher_alpha):
    teacher_rev_alpha_list = teacher_alpha_list.copy()
    teacher_rev_alpha_list.reverse() # sort into reverse alphabetical order
    return teacher_rev_alpha_list
        
def display_lists(teacher_list, teacher_alpha_list, teacher_rev_alpha_list):
    print() # blank line
    print("Your favourite teachers ranked are:", teacher_list)  # list in order of entry
    print("Your favourite teachers alphabetically are: {}". format(teacher_alpha_list))
    print("Your favourite teachers in reverse alphabetical order are: {}".format(teacher_rev_alpha_list))
 
def main()"
    print("Welcome to the Favourite Teachers Program")
    print() # blank line
    
    # get first four favourite teachers
    teacher_list = get_names()

    # Create list sorted alphabetically
    teacher_alpha_list = sort_alpha(teacher_list)

    # Create list sorted reverse alphabetically
    teacher_rev_alpha_list = sort_rev_alpha(teacher_alpha_list)

        
    # Display teachers in different orders
    display_lists(teacher_list, teacher_alpha_list, teacher_rev_alpha_list):
    
    # Then list the top two teachers
    print() # blank line
    print("Your top two teachers are: {} and {}".format(teacher_list[0], teacher_list[1]))
    
    # Then list the next two teachers
    print("The next two teachers are: {} and {}".format(teacher_list[2], teacher_list[3]))
    
    # Then list the last teacher
    print("Your last favourite teacher is: {}".format(teacher_list[-1]))
    
    # Display number of teachers in list
    print("Your have a total of {} favourite teachers.".format(len(teacher_list)))
    
    # Get a new favourite teacher
    new_teacher = input("Oops {} is no longer your favourite teacher. Who is your new FAVOURITE teacher: ".format(teacher_list[0]))
    new_teacher = new_teacher.title() # convert to title format
    teacher_list.insert(0, new_teacher)  # Place new name first in list
    
    # Sort lists again 
    teacher_alpha = teacher_list.copy()
    teacher_alpha.sort() # sort alphabetically
    teacher_revalpha = teacher_alpha.copy()
    teacher_revalpha.reverse() # sort reverse alphabetically
    
    # Display teachers in different orders
    print() # blank line
    print("Your favourite teachers ranked are:", teacher_list)  # list in order of entry
    print("Your favourite teachers alphabetically are: {}". format(teacher_alpha))
    print("Your favourite teachers in reverse alphabetical order are: {}".format(teacher_revalpha))
    
    # Then list the top two teachers
    print() # blank line
    print("Your top two teachers are: {} and {}".format(teacher_list[0], teacher_list[1]))
    
    # Then list the next two teachers
    print("The next two teachers are: {} and {}".format(teacher_list[2], teacher_list[3]))
    
    # Then list the last teacher
    print("Your last favourite teacher is: {}".format(teacher_list[-1]))
    
    # Display number of teachers in list
    print("Your have a total of {} favourite teachers.".format(len(teacher_list)))
    
    # Remove a teacher
    removed_teacher = input("You've decided that you no longer like a teacher. Which teacher would you like to remove from the list: ")
    teacher_list.remove(removed_teacher)
    
    # Display in order
    
    # resort alphabetically and display
    
    # resort reverse alphabetically and display


if __name__ == "__main__":
    main()
