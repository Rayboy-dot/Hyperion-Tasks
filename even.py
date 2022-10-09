# Asking user to enter a number

input_number= int(input("Enter a number: "))
count = 1

while count <= input_number:
    if count % 2 == 0:  # Skipping odds numbers, keeping only even numbers
        print(count)

    count = count + 1 