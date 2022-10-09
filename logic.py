# Task: write a program with a logic error

number1 = int(input("\nEnter a first number:"))
number2 = int(input("Enter a second number: "))
average = number1 + number2 / 2

print(f"the average number of {number1} and {number2} is {average}")

# Because of the order of operations in arithmetic, the program will not give the correct answer
# To rectify this problem ,we should add parentheses average = (number1 + number2)/2