#!/usr/bin/env python3

# Prompt for user name
# If user in system user list, Welcome user
# If user not in system, say "sorry you do not have an account and Goodbye"
# List current shipping prices
# Prompt for how many items to ship
# State how much the shipping cost will be
# Prompt if the order should be places
# If yes, state shipping the items

# Functions
def header():
    print("Welcome to the Shipping Accounts Program")
    print() # blank line

def user_list():
    users = ["me", "you", "us", "them"]
    return users

def qty_to_cost(min, to_or_over, max, cost):
    print("Shipping orders {} to {}:\t\t${} each".format(min, max, cost))

def qty_over_cost(min, to_or_over, cost):
    print("Shipping orders over {}:\t\t${} each".format(min, cost))

def shipping_rates():
    rates = [(0, "to", 100, "5.10"),\
    (100, "to", 500, "5.00"),\
    (500, "to", 1000, "4.95"),\
    (1000, "over", "4.80")]
    return rates

def current_shipping_prices(rates):
    print("Current shipping prices are as follows:")
    print() # blank line
    for j in rates:
        if "to" in j:
            (a,b,c,d) = j
            qty_to_cost(a,b,c,d) #(0, "to", 100, "5.10") for example
        elif "over" in j:
            (a,b,d) = j # no maximum "c"
            qty_over_cost(a, b, d) # (1000, "over", "4.80") for example

def calc(qty):
    if qty > 1000:
        price = 4.8
    elif qty >= 500:
        price = 4.95
    elif qty >= 100:
        price = 5
    else:
        price = 5.1
    cost = qty * price
    return (cost, price)
        
    

def main():

    header()
    
    name = input("Hello, what is your username: ")
    print() # blank line
    
    if name not in user_list():
        print("You do not have an account. Goodbye.") # not a valid user - program stops here
    else:
        print("Hello {}. Welcome back to your account.".format(name))
    
        current_shipping_prices(shipping_rates())
    
        print() # blank line
        qty = input("How many items would you like to ship: ")
        qty = int(qty) # convert input string type to integer
    
        (cost, price) = calc(qty)
    
        print("To ship {} it will cost you ${:.2f} at ${} per item".format(qty, cost, price))
    
    print() # blank line
    y_or_n = input("Would you like to place this order (y/n): ")
    
    if y_or_n == "y":
        print("Okay. Shipping your {} items".format(qty))
    elif y_or_n == "n":
        print("Okay. Not shipping anything.")
    
    
if __name__ == "__main__":
    main()
