str_manip = input("Please enter a sentence:")

print(len(str_manip))

# replace every occurence of last letter with @
print(str_manip.replace(str_manip[-1], "@"))

# print in reverse the last 3 characters
print(str_manip[-1] + str_manip[-2] + str_manip[-3][::-1])

# printing a 5 letter word made of first 3 and last 2 in reverse
print(str_manip[0:3] + str_manip[-2] + str_manip[-1])

# Displaying each word
print(str_manip.replace(str_manip[-1], "@"))
print(str_manip[-1] + str_manip[-2] + str_manip[-3][::-1])
print(str_manip[0:3] + str_manip[-2] + str_manip[-1])