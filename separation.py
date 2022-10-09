# Task: Create a program that input a sentence and then displays each word on a separate line
# Explanation:
# Request users to input a phrase
# Create a variable that contains different words by splitting the sentence inputed by the user
# Using the for loop, we print the word on different lines


sentence = input("\nEnter a sentence: ")
words = sentence.split()

for word in words:
    print(word)
