# Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove 
# duplicates and display the unique customer IDs.

# Example Code:

# customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

customer_ids_set = set(customer_ids)

print(customer_ids_set)
