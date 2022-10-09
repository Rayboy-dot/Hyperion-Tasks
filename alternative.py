# Task: creating a program that alternates each character of the string by making an uppercase and then a lowercase character
# Explanation:
# Request user to input a string 
# Create a variable containing the lenght of the string inputed
# Create an alternative variable containing an empty space
# Use the for loop statement.for each character in the lenght of the sentence, if the number is even we make it an uppercase of it, else we lowercae it
# The final string to print is equal to the indexed character from the inputed string plus teh alternative string
  

sentence = input("\nEnter a sentence: ")

sentence_len = len(sentence)

alt_sentence = ""

for character in range(sentence_len):
    if character % 2 == 0:
        alt_sentence += sentence[character].upper()
    else:
        alt_sentence += sentence[character].lower()
        
print(alt_sentence)
