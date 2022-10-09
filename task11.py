# This program is capable of diplaying the time table of any number inputed by the user
# Start by asking the user to enter any number and display the message the time table of the number inputed is.
# Use the for loop. The end index is set to 13 but excluded from the range (). Calculate the product to be displayed.

number = int(input("\nEnter any number: "))

print(f"The {number} times table is: ")

for count in range(1, 13):                             
    product = number * count  
    print(f"\n{number} x {count} = {product}")