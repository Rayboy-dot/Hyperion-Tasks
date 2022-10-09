# Task: creating a programm that strips a set of characters from a string
# Explanation:
# Requesting users to input a string and then ask them to input characters they would like to make disappear
# CReate a new string with the user's inputed characters to make disapear and use the split function
# Use a for loop with the replace function on the users inputed phrase. We replace with an empty string.


string_input = str(input("\nEnter a phrase: "))
character_choice = input("Enter the character you would like to make disappear: ")
replacement = character_choice.split(",")

for letter in replacement:
    string_input = string_input.replace(letter, '')

print(string_input)



