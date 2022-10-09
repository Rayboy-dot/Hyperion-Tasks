age = 18

# Ask user to enter their birth year:

birth_year = int(input("\nPlease enter the year you were born:"))
current_year = 2022

# Calculate user age:

user_age = current_year - birth_year

if user_age >= 18:
    print("Congrats you are old enough.")