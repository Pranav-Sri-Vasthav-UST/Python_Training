# '''
# Upgrade the code to display the minimum and maximum of the list
# '''

# Input

print("This app Gives Maximum and Minimum numbers from your inputs")
print("-"*80)

print("Enter your inputs: (! to quit) ")

# Collect the data from the user from the console
input_numbers = []   # Container for user input number

while True: 
    # Get the input
    user_input = input("-> ")

    # Check if the input is the terminating condition
    if(user_input == '!'):
        break

    # Otherwise, validate if it is an integer and add to the container
    if( user_input.isdigit() ):
        input_numbers.append(int(user_input))

# ----------------------- DEBUG statements -------------------------------- #
print("INFO [input_number] -> ", input_numbers)
# ------------------------------------------------------------------------- #

# Process

# Go through every number using inbuit methods and find maximum and minimum number

maximum_number = max(input_numbers)
minimum_number = min(input_numbers)

# output

print("-"*80)
print('Minimun and Maximum -> ', minimum_number, maximum_number)