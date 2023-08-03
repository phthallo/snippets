import sys

# Set up a list for our code to work with that omits the first CLI argument, 
# which is the name of our script (list_iteration.py)
order_of_succession = sys.argv
order_of_succession.pop(0) #This gets rid of the first argument, which is us calling the list_iteration.py file

# Now, order_of_succession is ready for us to work with
for index, item in enumerate(order_of_succession, start=1): #begin with 1 and not 0
    print(f"{index}. {item}")
