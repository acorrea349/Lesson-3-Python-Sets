# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a 
# competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# 1. Destinations that both airlines fly to.

# 2. Destinations unique to your airline.

# 3. Whether there are any destinations that neither airline shares.

# Example Code:

# our_routes = {"LAX", "JFK", "CDG", "DXB"}
# competitor_routes = {"JFK", "CDG", "LHR", "BKK"}




our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#task 1 common destinations
def common_destinations():
    common_elements = our_routes.intersection(competitor_routes)
    return common_elements

#task2 unique to our routes
def unique_to_our_routes():
    only_our_route = our_routes.difference(competitor_routes)
    return only_our_route

def unique_to_both():
    both_airlines = our_routes.symmetric_difference(competitor_routes)
    return both_airlines


def main():
    while True:


        try:

            user = int(input("Welcome to our Flight Route Comparison App \nMenu:\n1. Destinations that both airlines fly to.\n2. Destinations unique to your airline.\n3. Whether there are any destinations that neither airline shares.\n4.Exit Program \nSelect 1, 2, 3 or 4: "))


            if user == 1:
                print(common_destinations())
            
            elif user == 2:
                print(unique_to_our_routes())
            
            elif user == 3:
                print(unique_to_both())

            elif user == 4:
                break

            else:
                print("Please enter a valid option.")
    
        except ValueError:
            print("Please enter a valid option in numeric form.")

main()
print("Thank you for usinf the Flight Route Comparison App")