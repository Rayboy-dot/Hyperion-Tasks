# Defining two variables, 1 for the user input as a string and 1 for incorrect names as a list
# Use the while loop to loop through until the correct name is inputed

user_input = ("")
incorrectNames = []

print("\n")

while user_input != "John":
    
    user_input = (input("Enter a name: "))
    
    incorrectNames.append(user_input)                       # Add all incorrect names inputed to the list as long as the inputed name is not John
    
    if user_input == "John":
        break                                               # Break from the loop when inputed name is John to avoid an infinite loop
    
print(f"Incorrect names are :{incorrectNames[:-1]}")        # Print out the list of all incorrect names minus John the last name inputed