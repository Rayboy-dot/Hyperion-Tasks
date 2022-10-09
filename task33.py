import math

# Task1 : create a while loop to display count down from 20 to 0
# '''Explanation: count set at 21 as 20 will be included in the count. Condition is 
# >=1. This time we are not increasing the value but decreasing by 1 to reverse the loop'''.

count = 21

while count >= 1:
    count -= 1
    print(count)


# Task2:create a loop displaying even number between 1 and 20
# Start index is 1 and end index is 21 but will not be include in count.
# Setting the condition by using the if statement and the modulus by 2 opeator
# Ues the for loop and print

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Task3: create a loop that will produce a * in rows output
# The end index is 6 but we will only have 5 rows as the 6th is not included
# The outer loop while print the number of rows which is 5
# The inner will print the stars and we change lines after each iteration.

for i in range(6):
    for j in range(i):
        print("*", end='')
    print('')


# import math library.
# Getting the two integers we want to find the gcd.
# Find the the greatest common divisor of two integers'
# I found this method on w3schools.com. Pretty simple using gcd built in function.

number1 = int(input("Enter a  first number: "))
number2 = int(input("Enter a second number: "))
blank = 0

if number1 < number2:
    smallest = number1
else:
    smallest = number2

for value in range(1, smallest):
    if (number1 % value == 0) and (number2 % value == 0):
        blank = value
print(blank)


# This simple method with a built in function can also be used.

print(math.gcd(number1, number2))






